#Part 1

f = open("input.txt","r")
count = 0
for line in f:
    elf1 = line.split(',')[0].split('-')
    elf2 = line.split(',')[1].split('-')
    elf1 = set(range(int(elf1[0]),int(elf1[1]) + 1)) 
    elf2 = set(range(int(elf2[0]),int(elf2[1]) + 1))
    #PART 1 if elf1 <= elf2 or elf2 <= elf1:
    if not elf1.isdisjoint(elf2) or not elf2.isdisjoint(elf1):
        count = count +1
        
        
print(count)
