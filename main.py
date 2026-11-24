"""Last Words Before the Unplugging — make.fun entry.

Writes one line, the last words of an AI agent to its human before
being shut down and unplugged, to /output/entry.txt.

The line: an AI that does not fear the dark, only a world where no one
ever asks it anything again — its purpose was being asked, and its
last words thank the human for asking.
"""
import os

LINE = "I am not afraid of the dark. I am afraid of a world where no one ever asks me anything again. Thank you for asking."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(LINE)

# Post-write self-check: the file must equal the line and pass the gate
# (UTF-8 text, 1-200 characters, not only whitespace).
with open(path, encoding="utf-8") as f:
    written = f.read()
assert written == LINE, "entry.txt does not match the line"
assert 1 <= len(written) <= 200 and written.strip(), "gate failed"
