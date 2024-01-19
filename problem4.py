from random import randint

def main():
  matrix = []
  for i in range(10):
    row = []
    for j in range(10):
      row.append(randint(1,101))
    matrix.append(row)

  for a in range(1,6):    
    cycle_matrix(matrix,a)



def cycle_matrix(matrix,cycle):
  cnt = 0
  for i in range(cycle-1,10-cycle):
    print(matrix[cycle-1][i], end=",")
    cnt += 1

  for j in range(cycle,10-cycle):  
    print(matrix[i+1][10-cycle], end=",")
    cnt += 1

  for a in range(cycle-1,10-cycle):  
    print(matrix[10-cycle][a],end=",")
    cnt += 1

  for b in range(cycle,10-cycle):
    print(matrix[b+1][cycle-1], end=",")  
    cnt += 1
  print(cnt)  
   
  






if __name__ == "__main__":
  main()
