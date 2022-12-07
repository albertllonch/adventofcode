# Day 2
import numpy as np

def getTotalScore(scores):
    input_dict = {"X":0,"Y":1,"Z":2,"A":0,"B":1,"C":2}
    totalScore = 0
    file = open("input.txt","r")
    for line in file:
        a,b = line.strip().split(" ")
        totalScore = totalScore + scores[input_dict[a],input_dict[b]]
    file.close()
    return totalScore

scores = np.matrix('4 8 3; 1 5 9; 7 2 6')
print(getTotalScore(scores))
scores2 = np.matrix('3 4 8; 1 5 9; 2 6 7')
print(getTotalScore(scores2))


