import sys
from pprint import pprint
import time
import numpy as np

if len(sys.argv) != 2:
    print("Enter a file path (usage: python <script> <input_path>)")
    quit()
else:
    path = sys.argv[1]


file = open(path).readlines()

time = "".join([t for t in file[0].strip().split(" ") if t != ''][1:])
distance = "".join([d for d in file[1].strip().split(" ") if d != ''][1:])
time = int(time)
distance = int(distance)

def scenarios(time_record, dist_record):
    combos = []
    for i in range(time_record):
        # i = hold time & speed
        remaining_time = time_record - i
        dist_traveled = i * remaining_time
        if dist_traveled > dist_record:
            combos.append((i, dist_traveled))
    return combos

combos = scenarios(time, distance)

print(len(combos))