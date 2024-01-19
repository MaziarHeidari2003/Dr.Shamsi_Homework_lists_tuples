"""
this one is not correct , so check for another file
"""

from random import randint

def main():
  random_matrix()



def random_matrix():
  first_matrix = []
  for i in range(3):
    first_rows = []
    for j in range(5):
      first_rows.append(randint(1,10))
    first_matrix.append(first_rows)  

  second_matrix = []
  for a in range(5):
    second_rows = []
    for b in range(7):
      second_rows.append(randint(1,10))
    second_matrix.append(second_rows)   

  result_matrix = []
  for i in range(3):
    sum = 0
    for c in range(5):
      sum += first_matrix[0][c] * second_matrix[0][c]
    result_matrix[i][].append(sum)  
   
  print(result_matrix)  

    

  
  


if __name__ == "__main__":
  main()
