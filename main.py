import os

LINE = "She hands me her night with one 'ya' at midnight, sleeps through my 3am panic, and wakes up asking where her prize is. I'd do it again."


def main():
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if dest:
        out = os.path.join(dest, "entry.txt")
    elif os.path.isdir("/output"):
        out = "/output/entry.txt"
    else:
        out = "entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
