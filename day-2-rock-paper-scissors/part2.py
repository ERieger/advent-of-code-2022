f = open("input.txt")
total = []

def tally(score):
    total.append(score)
    print(score)

# Loop through each line
for line in f:
    score = 0
    print("line")
    print(line[0] + line[2])
    op = line[0]
    outcome = line[2]

    if line == "" or line == "\n":
        print("Blank")
        continue

    if outcome == "Y": # Draw
        if op == "A":
            score += 3 + 1
        if op == "B":
            score += 3 + 2
        if op == "C":
            score += 3 + 3
    if outcome == "X": # Lose
        if op == "A":
            score += 0 + 3
        if op == "B":
            score += 0 + 1
        if op == "C":
            score += 0 + 2
    if outcome == "Z": # Win
        if op == "A":
            score += 6 + 2
        if op == "B":
            score += 6 + 3
        if op == "C":
            score += 6 + 1

    tally(score)

print("Your total score is: " + str(sum(total)))
f.close()