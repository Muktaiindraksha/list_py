marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
totalMarks=0
for i in range (3):
    for j in range (5):
        totalMarks = totalMarks+marks[i][j]
print(totalMarks)

