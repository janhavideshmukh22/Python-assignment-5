a = int(input("Enter number of words to enter : "))
word_list = []
occurrences = {}

for i in range(0,a):
  a = input("Enter the word: ")
  word_list.append(a)
  
for i in word_list:
    if i in occurrences:
      occurrences[i] += 1
    else:
      occurrences[i] = 1

print("\n",word_list,"\n")

for key,value in occurrences.items():
  print("The occurence of {0} in the list is {1}.".format(key,value))
print()
