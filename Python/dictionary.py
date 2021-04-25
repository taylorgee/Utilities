from pprint import pprint

matrix = {'friends': ['Jazzy', 'Rachael', 'Hayden'], 
          'fruits': ['apple', 'banana', 'orange'], 
          'family': {'mama': 'lily'}}

rachael = matrix['friends'][1]
print(rachael)

print(f'Rachael is {rachael}')
print(matrix['fruits'])

banana = matrix['fruits'][1]
print(banana)

# index = using index to find an element position in a list
x = matrix['fruits'].index('banana')
print(x)
y = matrix['fruits'][x]
print(y)

pprint(matrix)

print()
print(matrix['family']['mama'])