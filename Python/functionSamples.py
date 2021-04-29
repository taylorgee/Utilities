def add(number1=10, number2=100):
    """
    Add two numbers
    
    Parameters 
       number1 <int>: a number to add
       number2 <int>: a second number to add
       
    Return
       The result
    """
    
    result = number1 + number2
    print(f'{number1} + {number2} = {result}')
    return result

def subtract(x, y=2):
    """
    Subtract two numbers
    
    Parameters
       x <int>: a number to subtract
       y <int>: a second number to subtract
       
    Return
       The result   
    """
    result = x - y
    print(f'{x} - {y} = {result}')
    #return result



addResult = add(9, 5)
print(f'addResult = {addResult}')
add()
add(5)

subtractResult = subtract(4, 7)
print(f'subtractResult = {subtractResult}')
