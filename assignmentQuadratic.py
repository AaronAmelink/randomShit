#Name: Aaron Amelink
#Date: Feb 23


a = int(input(""))
b = int(input(""))
c = int(input(""))
x = 0
y = (a*x)**2 + b*x + c
for x in range(1,10):
  
  lastY = y
  y = (a*x)**2 + b*x + c

  if (lastY < 0 and y > 0) or (lastY > 0 and y < 0):
    print("y = 0 occurs between:", x-1, x)

  if y == 0:
    print("y = 0 at:", x)

  