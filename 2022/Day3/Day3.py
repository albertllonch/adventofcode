import string

def existsX(arr,x):
    for e in arr:
        if e == x:
            return True
    return False

points = {}
x = 1 
for i in string.ascii_lowercase:
    points[i] = x
    x = x + 1
for i in string.ascii_uppercase:
    points[i] = x
    x = x + 1
file = open("input.txt","r")
sumPrio = 0
for line in file:
    a,b = line[:int(len(line)/2)], line[int(len(line)/2):]
    for i in a:
        if existsX(b,i):
            sumPrio = sumPrio + points[i]
            break

print(sumPrio)
file.close()
