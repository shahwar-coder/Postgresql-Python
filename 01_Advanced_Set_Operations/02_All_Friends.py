"""
The Union (all unique combined)
"""

# Define sets
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# Combine all unique people from both sets
all_friends = friends.union(abroad)

# Print result
print(all_friends) # {'Bob', 'Rolf', 'Anne'}