#Cecilia Zacarias
#2/27/2020

#Problem #3 is a function the multiplys all the numbers in a list. We are going to use the following list [5,2,7,-1

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((5,2,7,-1)))
