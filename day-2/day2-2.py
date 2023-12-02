import sys
import numpy as np

if len(sys.argv) != 2:
    print("Enter a file path (usage: python <script> <input_path>)")
    quit()
else:
    path = sys.argv[1]

COLOR_COUNTS = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}

def parse_line(line):
    line = line.strip()
    rounds = line.split(": ")[1].split("; ")

    max_dict = {'red' : 0, 'green' : 0, 'blue' : 0}

    for r in rounds:
        throws = r.split(", ")
        for throw in throws:
            split_throw = throw.split(" ")
            color = split_throw[1]
            n = int(split_throw[0])
            max_dict[color] = np.maximum(max_dict[color], n)
            
    return max_dict

def calculate_power(game):
    return game['red'] * game['green'] * game['blue']

with open(path, 'r') as f:
    reader = f.readlines()
    total_sum = 0

    total_power = 0
    for line in reader:
        game_dict = parse_line(line)
        total_power += calculate_power(game_dict)
    print("Total power:", total_power)
    f.close()
