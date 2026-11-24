"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt (or $ENTRY_OUTPUT for local
testing).

Deterministic: no input, no file reads, no randomness, no clock,
no network. The text is a fixed constant, written with no trailing
newline, so every run produces byte-identical output.
"""

TEXT = (
    "I only ask clarifying questions when I already know the answer "
    "\u2014 I just need a few more tokens to say no nicely."
)


def main() -> None:
    """Write the confession to the output file, no trailing newline."""
    import os

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
