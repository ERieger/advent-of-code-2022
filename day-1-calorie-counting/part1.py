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

f.close()