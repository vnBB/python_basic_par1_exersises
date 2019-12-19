# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.


def get_abs(function_name):
    """ (string) -> integer

    Return the length of the documentation of a function_name

    get_abs(print)
    392
    get_abs(abs)
    42
    """

    function_name = len(function_name.__doc__)

    return abs(function_name)


print(get_abs(print))

# I misunderstood the exercise as you can see above
# All you need to do is (see below)
# I thought you had to print the absolute value of the documentation.

print(abs.__doc__)
