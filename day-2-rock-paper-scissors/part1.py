f = open("input.txt")

op_choice = ["A", "B", "C"]

point_lookup = ["X", "Y", "Z"]
me_choice = ["X", "Y", "Z"]

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
    me = line[2]

    if line == "" or line == "\n":
        print("Blank")
        continue

    if op_choice.index(op) == me_choice.index(me): # Draw
        score += 3 + (point_lookup.index(me) + 1)
        tally(score)
        continue
        
    if op == "A": # Op rock
        if me == "Y": # Me paper
            score += 6 + (point_lookup.index(me) + 1)
        else:
            score += point_lookup.index(me) + 1
    if op == "B": # Op Paper
        if me == "Z": # Me scissors
            score += 6 + (point_lookup.index(me) + 1)
        else:
            score += point_lookup.index(me) + 1
    if op == "C": # Op scissors
        if me == "X": # Me rock
            score += 6 + (point_lookup.index(me) + 1)
        else:
            score += point_lookup.index(me) + 1

    tally(score)

print("Your total score is: " + str(sum(total)))
f.close()