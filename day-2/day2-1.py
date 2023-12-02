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
    split1 = line.split(": ")
    id = split1[0].split(" ")[-1]
    rounds = split1[1].split("; ")
    for r in rounds:
        throws = r.split(", ")
        for throw in throws:
            split_throw = throw.split(" ")
            color = split_throw[1]
            n = int(split_throw[0])
            if n > COLOR_COUNTS[color]:
                return id, False

    return id, True

with open(path, 'r') as f:
    reader = f.readlines()
    total_sum = 0

    games = []
    for line in reader:
        games.append(parse_line(line))
    valid_game_ids = [int(i) for i, v in games if v]

    print("Total:", np.sum(valid_game_ids))
    
    f.close()
