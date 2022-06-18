a = int(input("Enter the start of range : "))
b = int(input("Enter the end of range : "))
c = int(input("Enter the number to divide from : "))

for i in range(a,b):
  if(i%c == 0):
    print(i)
