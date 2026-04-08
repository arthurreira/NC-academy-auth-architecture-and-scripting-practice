import re

def show_lines_with_numbers(file_path):
    # Regular expression to detect at least one digit
    pattern = re.compile(r'\d')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if pattern.search(line):
                print(line.strip())

# Example usage
show_lines_with_numbers("input.txt")