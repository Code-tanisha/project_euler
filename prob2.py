range1 = 10
first = 0
second = 1
 
print("\nfibonacci series is:")
print first
print second
 
for i in range(2, range1):
    next = first + second
    print next
 
    first = second
    second = next
