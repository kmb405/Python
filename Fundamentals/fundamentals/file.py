num1 = 42 #variable declaration #Numbers
num2 = 2.3 #variable declaration #Numbers
boolean = True #variable declaration #Boolean
string = 'Hello World' #variable declaration #Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration #Strings #initialize List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration #Boolean #Strings #intialize Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration #Strings #initialize Tuple
print(type(fruit)) #log statement #type check 
print(pizza_toppings[1]) #log statement #access value List
pizza_toppings.append('Mushrooms') #log statement #Strings #add value List
print(person['name']) #log statement #Strings #access value Dict
person['name'] = 'George'  #Strings #change value Dict
person['eye_color'] = 'blue' #Strings #change value Dict
print(fruit[2]) #log statement #access value Tuple

if num1 > 45: #if 
    print("It's greater") #log statement #Strings
else: #else
    print("It's lower") #log statement #Strings

if len(string) < 5: #length check #if
    print("It's a short word!") #log statement #Strings
elif len(string) > 15: #length check #else if
    print("It's a long word!") #log statement #Strings
else: #else
    print("Just right!") #log statement #Strings

for x in range(5): #for loop start #for loop increment
    print(x) #log statement #for loop stop
for x in range(2,5): #for loop start #for loop increment
    print(x) #log statement #for loop stop
for x in range(2,10,3): #for loop start #for loop increment
    print(x) #log statement #for loop stop
x = 0
while(x < 5): #while loop start
    print(x) #log statement
    x += 1 #while loop stop #while loop increment

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) #log statement
person.pop('eye_color') #Strings #access value Dict
print(person) #log statement

for topping in pizza_toppings: #for loop start #for loop increment
    if topping == 'Pepperoni': #Strings
        continue #for loop continue
    print('After 1st if statement') #log statement #Strings
    if topping == 'Olives': #Strings
        break #for loop stop #for loop break

def print_hello_ten_times(): #function #function parameter
    for num in range(10): #for loop start #for loop increment
        print('Hello') #log statement #Strings #for loop stop

print_hello_ten_times()

def print_hello_x_times(x): #function #function parameter
    for num in range(x): #for loop start #for loop increment
        print('Hello') #log statement #Strings #for loop stop

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function #function parameter
    for num in range(x): #for loop start #for loop increment
        print('Hello') #log statement #Strings #for loop stop

print_hello_x_or_ten_times() #funciton call #function arguement
print_hello_x_or_ten_times(4) #funciton call #function arguement


"""
Bonus section #multiline comment
"""

print(num3) #NameError: name <variable name> is not defined
num3 = 72
fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) #KeyError: 'favorite_team'
print(pizza_toppings[7]) #IndexError: list index out of range
  print(boolean) #IndentationError: unexpected indent
fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'