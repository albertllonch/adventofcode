import numpy as np

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
elf = 0
print(food)
for x in range(0,len(food)):
    currentFood = sum(food[x])
    if currentFood > maxFood:
        maxFood = currentFood
        elf = x
print("Elf "+ str(elf + 1) + " has more food: " + str(maxFood))
