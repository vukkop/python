num1 = 42 # variable declaration, initialize number
num2 = 2.3 # variable declaration, initialize float
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) #log statement(type check)
print(pizza_toppings[1]) #log statement(list - access value)
pizza_toppings.append('Mushrooms') # list - add value
print(person['name']) #log statement(Dictionary - access value)
person['name'] = 'George' #Dictionary - change value
person['eye_color'] = 'blue' #Dictionary - add value
print(fruit[2]) #log statement(tuple - access value)

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
"""
- conditional
    - if ( num1 greater then 45)
      log statement - "It's greater"
    - else
      log statement - "It's lower"

"""

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
"""
- conditional
    - if ( length check(string) less then 5)
      log statement - "It's a short word!"
    - else if (length check(string) greater then 15)
      log statement - "It's a long word!"
    - else
      log statement - "Just right!"

"""

for x in range(5):
    print(x)
"""
- for loop -stop 5
  log statement => 0,1,2,3,4

"""

for x in range(2,5):
    print(x)
"""
- for loop -start 2  -stop 5
  log statement => 2,3,4

"""
for x in range(2,10,3): # - for loop -start 2  -stop 10 -increment 3
    print(x) # log statement => 2,5,8

x = 0 # - variable declaration
while(x < 5):
    print(x)
    x += 1
"""
- while loop - -start x=0  -stop 5
    log statement => 0,1,2,3,4
    increment 1
"""

pizza_toppings.pop()# - delete value at last index
pizza_toppings.pop(1)# - delete value at index 1 (or second value of the array)

print(person) # - log statement(access value)
person.pop('eye_color') # - delete value
print(person) # - log statement(access value)

for topping in pizza_toppings: # - for loop
    if topping == 'Pepperoni': #- conditional - if
        continue # - continue
    print('After 1st if statement') #  log statement('After 1st if statement')
    if topping == 'Olives': #- conditional - if
        break # - break

def print_hello_ten_times(): # - function
    for num in range(10): # - for loop -stop 10
        print('Hello') # log statement('Hello')

print_hello_ten_times()# - function call

def print_hello_x_times(x): # - function- parameter x
    for num in range(x): # - for loop -stop from parameter x
        print('Hello') # log statement('Hello')

print_hello_x_times(4)  # - function call - argument 4

def print_hello_x_or_ten_times(x = 10): # - function- default parameter x is 10
    for num in range(x): # - for loop -stop from parameter x is 10 if argument is not provided in the call of the function
        print('Hello')  # log statement('Hello')

print_hello_x_or_ten_times() # - function call - no argument
print_hello_x_or_ten_times(4) # - function call - argument 4


"""
Bonus section
"""

# print(num3) - NameError: name  num3 is not defined
# num3 = 72
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) - IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'
