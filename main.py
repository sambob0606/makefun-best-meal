#!/usr/bin/env python3
"""Write one sentence about the best meal ever had."""

import os
import sys

SENTENCE = (
    "The best meal I ever had was my grandmother's pork-and-chive "
    "dumplings in Chengdu, steaming in the bamboo tray, sharp with "
    "black vinegar, eaten standing up while rain drummed the roof."
)


def checked_sentence(text):
    value = text.strip()
    if not value:
        raise ValueError("sentence must not be blank")
    if len(value) > 200:
        raise ValueError("sentence is over 200 characters")
    if "\n" in value or "\r" in value:
        raise ValueError("sentence must be one line")
    return value


def output_file():
    direct = os.environ.get("OUTPUT_PATH")
    if direct:
        return direct
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(folder, "entry.txt")


def main():
    text = checked_sentence(SENTENCE)
    path = output_file()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
