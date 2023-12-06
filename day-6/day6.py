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

times = [t for t in file[0].strip().split(" ") if t != ''][1:]
times = [int(t) for t in times]
distances = [d for d in file[1].strip().split(" ") if d != ''][1:]
distances = [int(d) for d in distances]

def scenarios(time_record, dist_record):
    combos = []
    for i in range(time_record):
        # i = hold time & speed
        remaining_time = time_record - i
        dist_traveled = i * remaining_time
        if dist_traveled > dist_record:
            combos.append((i, dist_traveled))
    return combos

print('race | time | distance')
print('----------------------')

combo_counts = []
for i, (t, d) in enumerate(zip(times, distances)):
    combos = scenarios(t, d)
    combo_counts.append(len(combos))
    print(f"{i: <8} {t: <8} {d: <8}",len(combos), combos)

print(np.prod(combo_counts))