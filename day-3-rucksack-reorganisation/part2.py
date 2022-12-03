f = open("input.txt")

scores = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def half(content):
    return len(content)/2

line = 1
group_inv = []
badges = []
total = 0

for rucksack in f:
    contents = list(rucksack)
    print(rucksack)
    
    if contents.count("\n") > 0:
        contents.remove("\n")
    
    group_inv.append(contents)

    if line == 3:
        common_items = list(
            set(group_inv[0]).intersection(group_inv[1], group_inv[2])
        )

        print(common_items)
        badges.append(common_items[0])
        group_inv = []
        line = 0

    line += 1

for item in badges:
    total += (scores.index(item) + 1)

print("The total importance score is: " + str(total))