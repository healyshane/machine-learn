#Shane Healy 22-SEP-2019

n=int(input("Enter No. "))

# Keep looping until reach 1
# Assumes the Collatz conjecture is true
while n != 1:
    print(n)
    if n%2 == 0:
        n = n/2
    else:
        n = (3*n)+1

print(n)