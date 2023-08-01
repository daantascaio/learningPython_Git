"""
Higher Other Function

first class functions 
"""

def salude(msg, nome):
    return f'{msg}, {nome}!'

def exec(function, *args):
    return function(*args)

print(exec(salude, 'Bom dia', 'Caio'))

print(exec(salude, 'God night', 'Cecília'))