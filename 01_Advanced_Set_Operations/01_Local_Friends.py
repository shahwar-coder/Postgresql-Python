"""
The Difference
"""

# Define sets
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# Find friends who are NOT abroad
local_friends = friends.difference(abroad)

# Print result
print(local_friends) # {'Rolf'}

# local_friends = abroad.difference(friends) , doing other way round gives empty set -> set()