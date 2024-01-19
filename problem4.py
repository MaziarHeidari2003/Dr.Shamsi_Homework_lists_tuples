from random import randint

def main():
  matrix = []
  for i in range(10):
    row = []
    for j in range(10):
      row.append(randint(1,100))
    matrix.append(row)

  for a in range(1,6):    
    cycle_matrix(matrix,a)



def cycle_matrix(matrix,cycle):

  for i in range(cycle-1,11-cycle):
    print(matrix[cycle-1][i], end=",")

  for j in range(cycle,10-cycle):  
    print(matrix[j][10-cycle], end=",")

  for a in range(10-cycle,cycle-2,-1):  
    print(matrix[10-cycle][a],end=",")

  for b in range(10-cycle-1,cycle-1,-1):
    print(matrix[b][cycle-1], end=",")  
  print()  
   



if __name__ == "__main__":
  main()
