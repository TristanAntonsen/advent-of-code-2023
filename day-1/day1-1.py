import re
import sys

if len(sys.argv) != 2:
    print("Enter a file path (usage: python <script> <input_path>)")
    quit()
else:
    path = sys.argv[1]

with open(path, 'r') as f:
    reader = f.readlines()
    total_sum = 0

    for line in reader:
        line = line.strip()
        digits = re.sub("[^0-9]", "", line)
        line_sum = digits[0] + digits[-1]

        total_sum += int(line_sum)
    f.close()

    print(f"Total: {total_sum}")
    