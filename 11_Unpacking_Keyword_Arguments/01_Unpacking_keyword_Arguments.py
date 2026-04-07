# Function that accepts keyword arguments
def print_user(**kwargs):
    print(kwargs)  # kwargs is a dictionary

    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Call function with named arguments
print_user(name="Shahwar", age=22, role="AI Engineer")


"""
Understanding **kwargs (Keyword Arguments)

Purpose
-------
Allow a function to accept a flexible number of named arguments.


------------------------------------------------------------
1️⃣ What is **kwargs?
------------------------------------------------------------

def print_user(**kwargs):

• **kwargs collects ALL named arguments into a dictionary
• "kwargs" = "keyword arguments"

Example Call:
print_user(name="Shahwar", age=22, role="AI Engineer")

Inside function:
kwargs = {
    "name": "Shahwar",
    "age": 22,
    "role": "AI Engineer"
}


------------------------------------------------------------
2️⃣ How It Works
------------------------------------------------------------

print(kwargs)

• Prints the full dictionary

for key, value in kwargs.items():

• Iterates over key-value pairs

Output:
name: Shahwar
age: 22
role: AI Engineer


------------------------------------------------------------
3️⃣ Why Use **kwargs?
------------------------------------------------------------

✔ Flexible input (no fixed parameters)
✔ Useful for dynamic data
✔ Common in frameworks (APIs, configs, LLM inputs)

Example:
You don’t know in advance what fields user will send


------------------------------------------------------------
4️⃣ Important Rules
------------------------------------------------------------

• kwargs is always a dictionary
• Keys must be strings
• Comes AFTER normal parameters

Example:
def func(a, b, **kwargs):


------------------------------------------------------------
5️⃣ Mental Model
------------------------------------------------------------

Normal args:
func(1, 2) → fixed positions

Keyword args:
func(name="A") → named inputs

**kwargs:
Collect ALL extra named inputs into one dictionary


------------------------------------------------------------
Key Takeaway
------------------------------------------------------------

**kwargs lets your function accept unlimited named inputs
and handle them dynamically as a dictionary.
"""