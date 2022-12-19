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


#part 2

def commonElement(arr):
    result = set(arr[0])
    for currSet in arr[1:]:
        result.intersection_update(currSet)
    return result - {'\n'}


file = open("input.txt","r")
sumPrio = 0
for count, line in enumerate(file):
    pass
totalLines = count + 1
file.seek(0)
for x in range(0,totalLines,3):
    arr3 = []
    arr3.append(file.readline())
    arr3.append(file.readline())
    arr3.append(file.readline())
    comm = commonElement(arr3).pop()
    sumPrio = sumPrio + points[comm]
print(sumPrio)
file.close()
