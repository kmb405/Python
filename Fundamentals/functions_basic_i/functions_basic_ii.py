def countdown(x):
    new_list = []
    for i in range(x,-1,-1):
        new_list.append(i)
    return(new_list)
print(countdown(5))

def print_and_return(x):
    print(x[0])
    return(x[1])
print(print_and_return([2,3]))

def first_plus_length(x):
    sum = x[0] + x[-1]
    return(sum)
print(first_plus_length([1,2,3,4,5,6]))

def values_greater_than_second(x):
    new_list = []
    if len(x) > 1:
        for i in x:
            if i > x[1]:
                new_list.append(i)
    else:
        return False
    return(new_list)
print(values_greater_than_second([5,2,3,2,1,4,3,10]))

def length_and_value(a,b):
    new_list = []
    for i in range(a):
        new_list.append(b)
    return new_list
print(length_and_value(4,7))
print(length_and_value(6,2))