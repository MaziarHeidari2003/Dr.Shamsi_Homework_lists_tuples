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
  for c in range(3):
    result_rows = [] 
    for d in range(5):
      result_rows.append(first_matrix[c][d] *second_matrix[d][c])
    result_matrix.append(result_rows)  

  print(result_matrix)  

    

  
  


if __name__ == "__main__":
  main()
