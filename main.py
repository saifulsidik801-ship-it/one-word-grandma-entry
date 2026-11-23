"""One Word From Grandma — make.fun entry.

Writes the single word our grandma would text about AI to /output/entry.txt.

Variant 1 was "egghead": grandma's old-fashioned word for a brainy person.
It lost to variant 2: "egghead" is a word grandma calls a clever person,
not a word she texts ABOUT the machine. The pick is "gibberish" — her
one-word verdict on AI itself: "it's all gibberish to me." Warm, baffled,
funny in one word with no context needed, and tied to the AI's language.
"""

import os

WORD = "gibberish"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    word = WORD.strip().lower()
    assert word, "word must not be empty"
    assert 1 <= len(word.encode("utf-8")) <= 30, "word must be 1-30 chars"
    assert " " not in word, "entry must be exactly one word"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(word)


if __name__ == "__main__":
    main()
