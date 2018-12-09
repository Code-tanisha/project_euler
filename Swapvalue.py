# Program to swap two values
x = input('Enter the value of x: ')
y = input('Enter the value of y: ')
# create a temporary variable and then swap values
temp = x
x = y
y = temp
print('Value of x after swapping is: {}'.format(x))
print('Value of y after swapping is: {}'.format(y))
