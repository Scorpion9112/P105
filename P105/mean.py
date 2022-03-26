import csv
import math

with open("number.csv") as f:
  dataReader=csv.reader(f)
  allData=list(dataReader)

allData.pop(0)

totalMarks=0

totalStudents=len(allData)

for i in allData:
  totalMarks+=float(i[1])

mean=totalMarks/totalStudents

print(mean)

squaredList=[]
scoreData=allData[1]
for score in scoreData:
  sub=int(score)-mean
  squares=sub**2
  squaredList.append(squares)

total=0

for squares in squaredList:
  total=total+squares

result=total/(totalStudents-1)
standardDeviation=math.sqrt(result)
print(standardDeviation)