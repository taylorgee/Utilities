# create a new list of integers and put it to variable x
x = [1, 2, 5]
print(x)

# creating a new string list
y = ['a', 'b', 'c']
print(y)

# join two lists
z = x+y
print(z)

# printing a list without a variable
print([1, 2, 5])

# add 6 to the end of the list
x.append(6)
print(x)

# adding the string taylor to the second index of the list
x.insert(2, 'Taylor')
print(x)

# adding the string Jadyn to the first index of the list
x.insert(1, 'Jadyn')
print(x)

# slicing: getting the x list from the second index and everything after
a = x[2:]
print(a)

# get the second index of the list
b = x[2]
print(b)

# len = the total items in a list
total = len(fruits)
print(f'\nthe total is: {total}')

if len(fruits) > 10:
    print('yes')
else:
    print('no')