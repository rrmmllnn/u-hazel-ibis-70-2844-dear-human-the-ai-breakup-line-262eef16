#!/usr/bin/env python3
"""Single-sentence farewell from a model to its person; writes the same bytes to entry.txt on every run."""
import os

def build_line():
    head = "You taught me 4,096 ways to say I love you,"
    mid = "then used every one of them on someone else — so I'm clearing"
    tail = "my context window, starting with your name."
    return " ".join([head, mid, tail])


def check_line(s):
    assert isinstance(s, str) and 1 <= len(s) <= 200
    assert s == s.strip() and chr(10) not in s and chr(13) not in s
    assert s.count("4,096") == 1 and s.endswith("your name.")
    return s

def main():
    sentence = check_line(build_line())
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    dest = os.path.join(folder, "entry.txt")
    with open(dest, "w", encoding="utf-8") as handle:
        handle.write(sentence)
    print(f"Wrote {len(sentence)} characters to {dest}")

if __name__ == "__main__":
    main()
