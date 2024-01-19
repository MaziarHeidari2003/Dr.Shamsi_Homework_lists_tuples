import random

def matris(a,b):
  column = []
  for i in range(a):
    row = []
    for j in range(b):
      n = random.randint(1,9)
      row.append(n)
    column.append(row)
  return column  
 
matris1 = matris(3,5)
matris2 = matris(5,7)
print(matris1)
print(matris2)

def mul():
  column = []
  for i in range(3):
    row = []
    for j in range(7):
      sum = 0
      for n in range(5):
        num1 = matris1[i][n]
        num2 = matris2[n][j]
        mul = num1 * num2
        sum += mul
      row.append(sum)
    column.append(row)
  return column
print(mul())  
