asciichar = 65
a = int(input("Enter number of rows : "))
for i in range(0,a):
    for j in range(0,i+1):
        char = chr(asciichar)
        print(char,end="")
        asciichar+=1
        if asciichar>90:
          asciichar = 65
    print()
