# A lambda function is an anonymous function.
# It's speciality is that it is a single line function and is often passed to other functions

def square(n):
    return n * n


print(square(4))

# Rewriting the above using lambda.
f = lambda n: n * n
print(f(4))

# The beauty of this comes when you use them in other functions

nums = [2, 4, 7, 12, 59, 8, 3, 65, 7]
# The inbuilt function filter can be used to filter an iterable input based on a function.
# The input function can be a complex function. If the work is straightforward, you can deploy a lambda function there.
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

# The inbuilt function map() is used to apply a some action to all inputs of an iterable
squares = list(map(lambda n: n*n ,evens))
print(squares)

# Finally, the reduce() function is used to reduce the data to a single value
from functools import reduce
sum = reduce(lambda a,b : a+b, squares)
print(sum)

