# Decorators enable us to add to an existing function without making modifications to it.
# A simple dividing function that will divide first input value by 2nd input value


def div(a, b):
    return a / b


print(div(4, 2))
print(div(2, 4))


# Let's say that I have a requirement to divide the largest by smallest, no matter what order it is
# How can I implement without touching the original code

# We define a smarter div function that takes another function as an input
def smart_div(function):
    # Within this function we define another function that takes the same number of arguments as the original function to which
    # We are adding features
    def worker(a, b):
        # Now we implement the features
        if a < b:
            a, b = b, a
        # and then call the original function. Note that the values passed have already been manipulated.
        return function(a, b)
    # Finally, we return the inner function
    return worker

# We are now re-defining the div() function in our code.
div = smart_div(div)

# And when you now call, it uses the new feature to calculate.
print(div(4, 2))
print(div(2, 4))
