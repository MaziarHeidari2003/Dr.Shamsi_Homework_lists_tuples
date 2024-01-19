num_list = []
for i in range(21):
  num = [i]
  num_list.append(num)

while True:
  user_num = int(input('Enter the number: '))
  num_list[user_num-1].append(user_num)
  if user_num == 0:
    break
for i in range(20):
  if len(num_list[i]) != 1 :
    print(i+1,':',len(num_list[i])-1)


