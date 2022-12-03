f = open("input.txt")

scores = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
matches = []
total = 0

def half(content):
    print(content)
    return len(content)/2

for rucksack in f:
    contents = list(rucksack)
    
    if contents.count("\n") > 0:
        contents.remove("\n")
    
    comp = int(half(contents))

    comp1 = contents[0:comp]
    comp2 = contents[comp:len(contents)]
    print("Compartment 1: " + str(comp1))
    print("Compartment 2: " + str(comp2))
    print("Bag: " + str(contents))

    shared = None
    for ic1 in comp1:
        for ic2 in comp2:
            if ic1 == ic2:
                print("Match: " + str(ic1) + ", " + str(ic2))
                shared = ic1
                break
            else:
                continue
    matches.append(shared)
    print(shared)

for item in matches:
    total += (scores.index(item) + 1)

print("The total importance score is: " + str(total))