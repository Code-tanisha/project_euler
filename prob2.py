c = 0
first = 0
second = 1
d= 0 
while c < 4000000:
	c = first + second
	first = second
	second = c
	if c%2 == 0:
		d = d + c
print("The highest fibonacci value under 4million is: " + str(c)) 
print("The sum of all EVEN fibonacci values under 4million is: " + str(d))
