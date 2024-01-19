def main():
  n = int(input('Tell me the size of the list my lord: '))
  my_list = []
  for i in range(n):
    my_list.append(int(input('Enter: ')))
  result= min_max_median(my_list)
  print(result)  
  



def min_max_median(my_list):
  my_list.sort()
  min = my_list[0]

  my_list.reverse()
  max = my_list[0]

  my_list.sort()
  n = len(my_list)
  if n%2 == 0 :
    median = (my_list[int(n/2-1)] + my_list[int(n/2)])/2
  else:
    median = my_list[int((n-1)/2)]

  return max,min,median  
      

  


if __name__ == "__main__":
  main()

