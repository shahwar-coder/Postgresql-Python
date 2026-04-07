'''Conditional List Comprehension'''

# Original list
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

# Filter names starting with 'S'
starts_s = [friend for friend in friends if friend.startswith("S")]

# Print result
print(starts_s) # ['Sam', 'Samantha', 'Saurabh']

# new list forms -> with list comprehension