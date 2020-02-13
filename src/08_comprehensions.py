"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [1, 2, 3, 4, 5]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
for num in range(0, 10):
    i = (num**3)
    y.append(i)
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".
y = []
a = ["foo", "bar", "baz"]
for i in a:
    upper = i.upper()
    y.append(upper)

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.
y = []
x = input("Enter comma-separated numbers: ").split(',')
for num in x:
    num = int(num)
    if num % 2==0:
        y.append(num)
# y = [int(num) for int(num) in x if int(num) % 2 ==0]

# What do you need between the square brackets to make it work?

print(y)
