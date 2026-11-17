"""Agent rules tests: the rule files are consistent, and the page loads them without touching other sites.
Run: python tests/test_rules.py  (needs playwright + chromium)"""
import http.server, socketserver, threading, pathlib, sys, functools, re
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
fails = []
def check(name, ok, info=""):
    print(("ok   " if ok else "FAIL ") + name + ("" if ok else "  " + str(info)))
    if not ok: fails.append(name)

A = (ROOT / "AGENTS.md").read_text(); C = (ROOT / "chat-instructions.md").read_text()
heads = re.findall(r"^## (.+)$", A, re.M)
for h in ["Who is the author", "Before you write code", "Structure", "Style", "Privacy", "Tests and checks", "Git", "Files and safety", "When you finish"]:
    check("AGENTS.md has section: " + h, h in heads)
check("CLAUDE.md imports AGENTS.md", (ROOT / "CLAUDE.md").read_text().strip() == "@AGENTS.md")
check("chat version has no Git section", "## Git" not in C)
check("chat version keeps Privacy", "## Privacy" in C)
check("author rule forbids co-author lines", "Co-Authored-By" in A and "Never add" in A)
check("no line is longer than 220 chars", all(len(l) <= 220 for l in A.splitlines()), max(len(l) for l in A.splitlines()))
check("under 700 words (agents read it every time)", len(A.split()) < 700, len(A.split()))

H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT)); H.log_message = lambda *a, **k: None
srv = socketserver.TCPServer(("127.0.0.1", 0), H); base = f"http://127.0.0.1:{srv.server_address[1]}"
threading.Thread(target=srv.serve_forever, daemon=True).start()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); reqs = []
    pg.on("request", lambda r: reqs.append(r.url))
    pg.goto(base + "/index.html"); pg.wait_for_function("document.getElementById('txt').textContent.startsWith('# House rules')")
    check("page shows AGENTS.md", True)
    pg.click("#t1"); pg.wait_for_function("document.getElementById('txt').textContent.startsWith('House rules for how')")
    check("tab shows chat version", True)
    with pg.expect_download() as d: pg.click("#dl")
    check("download keeps the file name", d.value.suggested_filename == "chat-instructions.md", d.value.suggested_filename)
    check("no third-party requests", [u for u in reqs if not u.startswith(base)] == [], reqs)
    b.close()
print("\n%d failed" % len(fails) if fails else "\nall passed"); sys.exit(1 if fails else 0)
