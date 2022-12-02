# Day 2
import numpy as np

input_dict = {"X":0,"Y":1,"Z":2,"A":0,"B":1,"C":2}
scores = np.matrix('4 8 3; 1 5 9; 7 2 6')
totalScore = 0
print(scores)
file = open("input.txt","r")
for line in file:
    a,b = line.strip().split(" ")
    totalScore = totalScore + scores[input_dict[a],input_dict[b]]

print(totalScore)
    

