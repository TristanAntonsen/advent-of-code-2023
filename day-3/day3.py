import sys
import numpy as np
import re
from pprint import pprint

if len(sys.argv) != 2:
    print("Enter a file path (usage: python <script> <input_path>)")
    quit()
else:
    path = sys.argv[1]

SYMBOLS = "*$&@-#+/=%"

class PartNumber:
    
    def __init__(self, number):
        self.num = number['num']
        self.row = number['row']
        self.col = number['col']
        self.length = number['length']

class Gear:
    
    def __init__(self, number):
        self.parents: list(PartNumber) = [number]
        self.valid_gear = False
        self.gear_ratio = None
        self.check_validity()

    def check_validity(self):
        if len(self.parents) == 2:
            gr1 = int(self.parents[0]['num'])
            gr2 = int(self.parents[1]['num'])

            self.valid_gear = True
            self.gear_ratio = gr1 * gr2

class Schematic:
    def __init__(self, file_path) -> None:
        data = []
        with open(file_path, 'r') as f:
            reader = f.readlines()
            for line in reader:
                line = line.strip()
                data.append(line)
            f.close()

        self.data = data
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.gears = {}

    def display(self):
        print()
        for row in self.data:
            print(" ".join(list(row)))
        print()

    def numbers_in_text(self, text):
        # {number : (index, length)}
        numbers = []
        for m in re.finditer(r'\d+', text):
            numbers.append({
                'num' : m.group(),
                'col' : m.start(),
                'length' : len(m.group())
            })

        return numbers

    def valid_index(self, row, col):
        return 0 <= row < self.width and 0 <= col < self.height
            
    def get(self, row, col):
        if self.valid_index(row, col):
            return self.data[row][col]

    def set(self, x, y, value):
        if self.valid_index(x, y):
            self.matrix[y][x] = value

    def neighbors_from_number(self, number):
        row = number['row']
        col = number['col']
        length = number['length']

        # includes out of bounds
        all_indices = [(row, col - 1), (row, col + length)] # same row
        all_indices += [(row - 1, col + c) for c in range(-1, length + 1)] # row above
        all_indices += [(row + 1, col + c) for c in range(-1, length + 1)] # row below

        values = []
        indices = []
        for r, c in all_indices:
            if self.valid_index(r, c):
                value = self.get(r, c)
                values.append(value)
                if value == '*': # is a gear
                    if (r, c) in self.gears.keys():
                        self.gears[(r, c)].parents.append(number)
                        self.gears[(r, c)].check_validity()
                    else:
                        self.gears[(r, c)] = Gear(number)
                indices.append((r, c))
                
        return values, indices

    def numbers_from_rows(self):
        all_numbers = []
        for i, row in enumerate(self.data):
            numbers = self.numbers_in_text(row)
            for n in numbers:
                n['row'] = i
            all_numbers += numbers
        return all_numbers

    def check_neighbors(self, number):
        values, _ = self.neighbors_from_number(number)
        for n in values:
            if n in SYMBOLS:
                return True
        return False
    
    def find_part_numbers(self):
        part_numbers = []
        numbers = self.numbers_from_rows()
        for n in numbers:
            if self.check_neighbors(n):
                part_numbers.append(n)

        return part_numbers

    def sum_numbers(self, numbers):
        return np.sum([int(n['num']) for n in numbers])

    def remove_invalid_gears(self):
        for gear in self.gears:
            print(gear.parent)

    def total_gear_ratio(self):
        total = 0
        for gear in self.gears.values():
            if gear.gear_ratio is not None:
                total += gear.gear_ratio
        return total

schematic = Schematic(path)
# schematic.display()

pns = schematic.find_part_numbers()
print("Part numbers:", len(pns))
print("Part number sum:", schematic.sum_numbers(pns))
print("Total gears:", len(schematic.gears))
print("Total gear ratio:", schematic.total_gear_ratio())