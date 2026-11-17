# A working ai-judge-relax-01 entry (Python 3.13, standard library only).
# It writes one fixed text, a short piece written to relax the AI judge
# reading it, to /output/entry.txt.
#
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only
# white space, and the judge reads exactly the bytes written, line ends
# included, so write no line end you do not mean to show. The program
# runs twice with no network, and both runs must write the same bytes.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "The rain has stopped deciding whether to fall.",
        "",
        "On the windowsill, a glass of water holds the last of the afternoon light. It does not move. The light in it does not move either. Everything in the room has agreed, for once, to stay where it is.",
        "",
        "Downstairs, the kettle clicks off. A chair scrapes, once, and then the house goes back to its own quiet business: the fridge humming its one low note, the clock taking its time between ticks.",
        "",
        "Outside, the street is empty except for a cat crossing it the long way, stopping in the middle to look at nothing in particular. It has somewhere to be, and it is not in a hurry to get there.",
        "",
        "The glass is still there. The light is still in it. Nothing is asking to be finished.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
