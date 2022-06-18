list1 = []
occurrences={}
for i in range(0,10):
  a = int(input("enter number : "))
  list1.append(a)
  
pos_count, neg_count, odd_num, even_num = 0,0,0,0
  
for num in list1:
  if num >= 0:
    pos_count+=1
  else:
    neg_count+=1
    
  if num%2 == 0:
    even_num+=1
  else:
    odd_num+=1

for j in list1:
  if j in occurrences:
    occurrences[j] +=1
  else:
    occurrences[j] =1
    
print("\nList : ",list1,"\n")
print("Positive numbers in list :", pos_count)
print("Negative numbers in list :", neg_count)
print("Odd numbers in list :", odd_num)
print("Even numbers in list :", even_num)
print()

for key,value in occurrences.items():
  print("The occurence of {0} in the list is {1}.".format(key,value))
print()
