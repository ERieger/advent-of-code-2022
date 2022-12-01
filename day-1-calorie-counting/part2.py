f = open("./input.txt")
totals = []
elf = 0

for food in f:
    if food == "\n":
        print(elf)
        totals.append(elf)
        elf = 0
    else:
        elf += int(food)

totals.sort(reverse=True)
print("The elf you want as your friend has " + str(totals[0]) + " calories.")
top3 = sum([totals[0], totals[1], totals[2]])
print("So we don't run out of snacks and starve here is the sum of the top 3 elves: " + str(top3))

f.close()