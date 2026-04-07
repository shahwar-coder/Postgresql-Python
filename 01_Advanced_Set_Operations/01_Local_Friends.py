# Define sets
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# Find friends who are NOT abroad
local_friends = friends.difference(abroad)

# Print result
print(local_friends) # {'Rolf'}