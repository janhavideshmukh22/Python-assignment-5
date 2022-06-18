a = int(input("Enter the start of range : "))
b = int(input("Enter the end of range : "))

for num in range(a,b+1):
  if num > 1:
    for i in range(2,num):
      if(num%i == 0):
        break
    else:
      print(num)
      
