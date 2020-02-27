#Cecilia Zacarias
#2/27/2020

#Problem #4 this python function takes a list of numbers and returns a new list with unique elements of the first list. we are going to use the following list [1,3,3,6,2,3,5] and using the append function as well.

def unique_list(i):
    x = []
    for a in i:
        if a not in x:
            x.append(a)
    return x

print (unique_list([1,3,3,3,6,2,3,5]))
