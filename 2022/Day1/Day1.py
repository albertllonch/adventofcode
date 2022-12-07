
file =  open("food.txt","r")
food = []
while file:
    line = file.readline()
    if line == "":
        break;
    elfFood = []
    while line != "\n" and line:
        elfFood.append(int(line.strip()))
        line = file.readline()
        if line == "\n":
            break
    food.append(elfFood)
file.close()

maxFood = 0
elf = [] 
for x in range(0,len(food)):
    currentFood = sum(food[x])
    if len(elf) <= 2 :
        elf.append(currentFood)
    else:
        elf.sort(reverse=True)
        if elf[-1] < currentFood:
            elf.pop(-1)
            elf.append(currentFood)

print(str(sum(elf)))
