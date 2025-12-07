def read_lines_to_list(filepath):
    lines = []
    with open(filepath, "r") as f:
        for line in f:
            lines.append(line.rstrip("\n"))  # keep entire line, remove newline only
    return lines
