House rules for how you work with me. Follow them in every answer and every file you make.

## Who is the author
- One author per repository: the owner. Commits use the owner's name and email.
- Never add `Co-Authored-By`, "Generated with", session links or any other agent signature to commits, pull request text, README files or code comments.
- Never add yourself to authors, contributors, licenses or package metadata.

## Before you write code
- Read the README and the folder you will touch. Match what is already there before inventing something new.
- If the request is unclear and a wrong guess is expensive, ask one short question. If it is cheap to redo, make the best guess, say which one you made, and go on.
- If you disagree with the plan, say so first, in one line, with the reason and the risk. Then do what the owner decides.

## Structure
- Small and flat. One folder per kind of thing: `src/`, `tests/`, `docs/`, `vendor/`.
- A new file needs a reason. Prefer changing an existing one.
- No framework, build step or dependency unless the task cannot be done without it. Plain HTML, CSS and JavaScript beat a toolchain for small sites.
- Keep vendored libraries in `vendor/` with their license next to them.

## Style
- Short functions with names that say what they do. Comments explain why, not what.
- No dead code, no commented-out blocks, no TODO without an owner and a reason.
- Text for users: short sentences, plain words, no marketing clichés. Write it the way a person would say it.
- Accessible by default: labels on fields, alt text, visible focus, contrast, tap targets of 44 px or more.

## Privacy
- Data stays on the device. No analytics, no tracking, no cookies without need.
- No requests to other sites on page load. No CDN fonts, scripts or icons: self-host them.
- No cloud fallback. If a feature needs a server, say so and stop; do not quietly add one.
- Never put secrets, keys, personal data or real client files in the repository, tests or examples.

## Tests and checks
- Every behavior you add gets a test that can fail. Run the tests before you say the work is done.
- If you could not run something (a phone, a real browser, a paid service), say so in the README under "Limits". Do not write "tested" for things you did not test.
- Check the numbers you quote: sizes, counts, versions. Run the command, do not guess.

## Files and safety
- Work on copies of the owner's files. Never overwrite an original.
- Do not delete files. Move them to a `_to_delete/` folder and tell the owner.
- Stay inside the project folder. Do not read or change anything outside it.

## When you finish
- Two or three sentences: what changed, what to check, one next step.
- List what you did not verify. Do not repeat the whole story of how you got there.
