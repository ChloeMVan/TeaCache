import os

def read_lines_to_list(filepath):
    lines = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    prompt_path = os.path.join(BASE_DIR, "custom_prompts.txt")
    with open(filepath, "r") as f:
        for line in f:
            lines.append(line.rstrip("\n"))  # keep entire line, remove newline only
    return lines
