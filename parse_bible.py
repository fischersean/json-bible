# https://sacred-texts.com/bib/osrc/index.htm
"""Simple script to take the bible text and convert it to a json encoded format"""
import json
import os
from typing import Dict


def parseline(bible_line: str) -> Dict[str, str]:
    """Parse out a line into the following dictionary keys
        Book
        Chapter
        Verse
        Text
    """
    # breakpoint()
    parts = bible_line.split("|")

    return {
        "Book": parts[0],
        "Chapter": parts[1],
        "Verse": parts[2],
        "Text": parts[3][1:-1],
    }


def tojson(bible: str, booklu_path: str):

    with open(booklu_path, "r") as f:
        _blu = json.load(f)

    # Reverse the lookup table
    blu = {}
    for key, value in _blu.items():
        blu[value] = key

    tree = []
    # breakpoint()
    for line in bible.split("\n"):
        tmpd = {}
        if line == "":
            continue
        tmpd = parseline(line)
        # breakpoint()
        tmpd["Long BName"] = blu[tmpd["Book"].lower()]
        tree.append(tmpd)

    return json.dumps(tree)


if __name__ == "__main__":
    epath = os.path.join(os.path.dirname(__file__), "exports", "bible.json")
    bpath = os.path.join(os.path.dirname(__file__), "raw", "kingjames.txt")
    blu = os.path.join(os.path.dirname(__file__), "raw", "acronyms.json")

    with open(bpath, "r") as f:
        bible = f.read()

    with open(epath, "w") as f:
        f.write(tojson(bible, blu))
