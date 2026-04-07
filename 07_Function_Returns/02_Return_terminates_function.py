def check_number(num):
    if num < 0:
        return "Negative number"

    print("This runs only if number is NOT negative")
    return "Positive number"


# Test cases
print(check_number(-5))
print(check_number(10))

# Negative number
# This runs only if number is NOT negative
# Positive number