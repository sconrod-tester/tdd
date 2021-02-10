def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtraction Function"""
    return x - y

def multiple(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Multiply Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return  x / y
