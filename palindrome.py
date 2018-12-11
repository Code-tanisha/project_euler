#Program to check is the string is palindrome or not.

my_str = "aiOPuhyIDhgjY"
# make it suitable for caseless comparison
my_str = my_str.casefold()
rev_str = reversed(my_str)
# check if the string is equal to the reversed string
if list(my_str) == list(rev_str):
print(" It is a palindrome")
else:
print("not a palindrome")
