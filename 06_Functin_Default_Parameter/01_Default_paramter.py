# Function with default value
def greet(name="Guest"):
    print("Hello", name)

# Calling without argument (uses default)
greet()

# Calling with argument (overrides default)
greet("Shahwar")

# Hello Guest
# Hello Shahwar