# Function that accepts any number of arguments
def multiply(*args):
    print(args)  # args is a tuple

    total = 1
    for arg in args:
        total = total * arg

    return total


# Call function with multiple arguments
print(multiply(1, 3, 5))

# (1, 3, 5)
# 15