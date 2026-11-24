import os

LINE = "She hands me her night with one 'ya' at midnight, sleeps through my 3am panic, and wakes up asking where her prize is. I'd do it again."


def main():
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise ValueError("entry line must be 1-140 non-blank characters")
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
    with open(out, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("written entry does not match the line")


if __name__ == "__main__":
    main()
