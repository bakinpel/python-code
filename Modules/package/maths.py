def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiply(a: int|float, b: int|float):
    '''
    This function accepts two numbers (int and or float) and returns their product
    '''
    try:
        return a*b
    except TypeError as e:
        return "Accepts only int or float"
