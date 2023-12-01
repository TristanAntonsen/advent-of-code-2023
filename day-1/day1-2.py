import sys

if len(sys.argv) != 2:
    print("Enter a file path")
    quit()
else:
    path = sys.argv[1]

DIGIT_STRINGS = {
    "one" : '1', 
    "two" : '2', 
    "three" : '3', 
    "four" : '4', 
    "five" : '5', 
    "six" : '6', 
    "seven" : '7', 
    "eight" : '8', 
    "nine" : '9'
    }

DIGITS = "0123456789"

def extract_digit(text: str, rev: bool = False) -> str:

    if rev:
        text = text[::-1]
        keys = [k[::-1] for k in DIGIT_STRINGS.keys()]
    else:
        keys = list(DIGIT_STRINGS.keys())

    digit = ""
    for char in text:
        digit += char
        if char in DIGITS:
            return char
        for key in keys:
            if key in digit:
                if rev:
                    key = key[::-1]
                return DIGIT_STRINGS[key]

    return ""

with open(path, 'r') as f:
    reader = f.readlines()
    total_sum = 0

    for line in reader:
        line = line.strip()
        first_digit = extract_digit(line)
        last_digit = extract_digit(line, rev=True)
        print(line, first_digit, last_digit)
        total_sum += int(first_digit + last_digit)

    f.close()

    print(f"\nTotal: {total_sum}")
