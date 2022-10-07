import json
import sys

MAX_CHAR_EASY = 150
MAX_CHAR_MEDIUM = 250
MAX_CHAR_HARD = 500

user_os = sys.platform

if user_os == "linux" or user_os == "darwin":
    encoding = "utf-8"

elif user_os == "win32":
    encoding = "mbcs"

# texts from 0-150 characters in length
with open("lib/easy.json", "r", encoding=encoding) as file:
    easy = json.load(file)

# texts from 151-250 characters in length
with open("lib/medium.json", "r", encoding=encoding) as file:
    medium = json.load(file)

# texts 251+ characters in length
with open("lib/hard.json", "r", encoding=encoding) as file:
    hard = json.load(file)


def check_text_length(f, filename, min_chars, max_chars):
    """
    Prints error on any line within file f, if the line's length
    is outside of min_chars and max_chars, inclusive.
    """
    line_num = 1

    for line in f:
        if len(line) < min_chars:
            print(f'ERROR: in "{filename}", line {line_num}')
            print(f"  {line}\n")
            print(
                f"Too few characters. This text has only {len(line)} characters, but expected at least {min_chars} characters.\n\n"
            )
        elif len(line) > max_chars:
            print(f'ERROR: in "{filename}", line {line_num}')
            print(f"  {line}\n")
            print(
                f"Too many characters. This text has {len(line)} characters, but expected at most {max_chars} characters.\n\n"
            )

        line_num += 1


# Validate all json files
check_text_length(easy, "lib/easy.json", 0, MAX_CHAR_EASY)
check_text_length(medium, "lib/medium.json", MAX_CHAR_EASY + 1, MAX_CHAR_MEDIUM)
check_text_length(hard, "lib/hard.json", MAX_CHAR_MEDIUM + 1, MAX_CHAR_HARD)
