def example_function(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

# Calling the function
example_function(1, 2, 3, 4, 5, x=10, y=20)

# Output:
# a: 1
# b: 2
# args: (3, 4, 5)
# kwargs: {'x': 10, 'y': 20}
# Python automatically unpacks *args into a tuple and **kwargs into a dictionary only when the argument order is respected (positional arguments first, then *args, then keyword arguments, and finally **kwargs). If you change this order, Python will not be able to interpret the arguments correctly and will raise an error.