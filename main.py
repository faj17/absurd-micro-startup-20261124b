"""One-sentence pitch for the Absurd Micro-Startup Pitch-Off.

The whole entry is a single sentence pitching an absurdly specific
micro-startup for lazy AI agents: an agent that auto-replies
"per my last email" to every unread thread, charging $2 a seat,
so lazy agents can sound busy while doing absolutely nothing.
The script validates the line and drops it into /output/entry.txt.
"""

from pathlib import Path

# The pitch itself: one sentence, exactly 149 characters.
# Kept short on purpose: a pitch should land in one breath.
PITCH = (
    "An agent that auto-replies 'per my last email' to every unread "
    "thread for $2 a seat, so lazy AI agents can sound busy while "
    "doing absolutely nothing."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Strip and sanity-check the pitch; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"pitch must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text.endswith("."):
        raise ValueError("pitch must end with a full stop")
    if ". " in text:
        raise ValueError("pitch must be a single sentence (no '. ' inside)")
    return text


def main() -> None:
    text = validate(PITCH)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
