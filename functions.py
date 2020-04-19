
# basic function, no i/p args and no return values
def hello():
    print("Hello World!", end=" ")
    print("How are you?")


# function with two input args and one return value
def add(x, y):
    return x + y


# function with two return values
def add_sub(x, y):
    return x + y, x - y


hello()
print(add(2, 3))
print(add_sub(2, 3))
