# List of users (id, username, password)
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4ssword"),
    (3, "username", "1234"),
]

# Create a dictionary mapping username -> full user tuple
username_mapping = {user[1]: user for user in users}

# Print result
print(username_mapping)


# {
#  'Bob': (0, 'Bob', 'password'),
#  'Rolf': (1, 'Rolf', 'bob123'),
#  'Jose': (2, 'Jose', 'longp4ssword'),
#  'username': (3, 'username', '1234')
# }