a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a+b>=c and b+c>=a and c+a>=b:
  s = (a+b+c)/2
  area = round((s*(s-a)*(s-b)*(s-c)) ** 0.5,2)
  print("Area is",area)
else:
  print("Triangle is not valid")
