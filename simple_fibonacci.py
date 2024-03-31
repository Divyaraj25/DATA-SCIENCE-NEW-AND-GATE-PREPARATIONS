a,b = 0,1
while a<1000:
    print(a)
    a,b = b,a+b
# with function
def fibonacci(limit:int):
    """
    gives a fibonacci series

    Args:
        limit (int): takes limit of fibonacci series
    """
    a_new,b_new = 0,1
    while a_new<limit:
        print(a_new)
        a_new,b_new = b_new,a_new+b_new
fibonacci(500) # returns a fibonacci series
print(fibonacci.__doc__) # prints a docstring of function
print(fibonacci.__annotations__) # gives a list of annotations in the function
