import sys
import numpy as np

if len(sys.argv) != 2:
    print("Enter a file path (usage: python <script> <input_path>)")
    quit()
else:
    path = sys.argv[1]

def parse_line(card):
    card = card.strip().split(": ")[1] # remove prefix
    card = card.split(" | ")
    winners = [int(n) for n in card[0].split(" ") if n != '']
    scratched = [int(n) for n in card[1].split(" ") if n != '']
    
    return winners, scratched
        
def determine_score(card):
    winners, scratched = parse_line(card)
    score = 0
    matches = 0
    for num in scratched:
        if num in winners:
            matches += 1
            if score >= 1:
                score *= 2
            else:
                score = 1

    return matches, score
    
with open(path, 'r') as f:
    reader = f.readlines()
    total_matches = 0
    total_score = 0
    for line in reader:
        matches, score = determine_score(line)
        total_matches += matches
        total_score += score

    f.close()

print("Total matches:", total_matches)
print("Total score:", total_score)