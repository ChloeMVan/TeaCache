import os

def read_lines_to_list(filepath):
    # n = 3
    # i = 0
    lines = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(BASE_DIR, filepath)
    with open(prompt_path, "r") as f:
        for line in f:
            lines.append(line.rstrip("\n"))  # keep entire line, remove newline only
            # if i == n:
            #     break
            # i+=1
    return lines
