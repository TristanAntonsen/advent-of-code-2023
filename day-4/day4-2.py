import sys

if len(sys.argv) != 2:
    print("Enter a file path (usage: python <script> <input_path>)")
    quit()
else:
    path = sys.argv[1]

def parse(line):
    card = line.strip().split(": ")[1] # remove prefix
    card = card.split(" | ")
    winners = [n for n in card[0].split(" ") if n != '']
    scratched = [n for n in card[1].split(" ") if n != '']

    return winners, scratched
 
def count_matches(winners, scratched):
    match_count = 0
    for num in scratched:
        if num in winners:
            match_count += 1

    return match_count

file = open(path).readlines()

counter = [1 for _ in range(len(file))]

for i, line in enumerate(file):
    # extract winning #s and scratched #s
    winners, scratched = parse(line)

    # find number of matches
    matches = len(set(winners) & set(scratched))
    print(f"Card {i} | {matches}")

    for j in range(matches):
        new_index = i + j + 1
        counter[new_index] += counter[i] # some help from reddit to figure this line out :)

print("Total cards:", sum(counter))