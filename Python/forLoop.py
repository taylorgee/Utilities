fruits = ['apple', 'banana', 'grapes']

# for loop to print each fruite one by one.
# \n is next line
# \t is tab
for fruit in fruits:
    print(f"\nmy favorite fruit is\n\t{fruit}")
  
print('\n\n') 

# enumerate = printing the index 
for number, fruit in enumerate(fruits):
    print(f"{number}: {fruit}")