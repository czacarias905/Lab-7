#Cecilia Zacarias
#2/27/2020

#Problem #2 write a function to check weather a number is in a given range. the range we are using is (1,10).

def test_range(n):
    if n in range (1,10):
        print(" %s is in the range"%str(n))
    else:
        print("The number is outside the given range.")

n = input("Type in any number to check the range")
test_range(15)
