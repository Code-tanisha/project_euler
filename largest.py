# Program to find the largest number among the three input numbers
a = 5
b = 6
c = 8
if(a >= b) and (a >= c):
  largest = a
elif(b >= a) and (b >= c):
  largest = b
else:
  largest = c

print("The largest number between",a,",",b,"and",c,"is",largest)
