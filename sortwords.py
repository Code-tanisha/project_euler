# Program to print the string in alphabetical order

my_str = input("Enter the string: ")
# break the string into list of words
words = my_str.split()
words.sort()
print("The sorted words")
for word in words:
 print(word)
