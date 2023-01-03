"""
Create a generator
"""
def generator(*args):
    for value in args:
        yield value * 10
        
for value in generator(1,2,3,4,5,6,7,8,9):
    print(value)
    
