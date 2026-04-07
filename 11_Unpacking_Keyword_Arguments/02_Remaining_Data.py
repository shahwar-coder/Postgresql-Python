# A simple function like an API call
def send_message(user, message=None, urgent=False, **kwargs):
    print("User:", user)
    print("Message:", message)
    print("Urgent:", urgent)
    print("Extra data:", kwargs)


# Call function
send_message(
    "Shahwar",
    message="Hello!",
    urgent=True,
    timestamp="10:30 AM",
    location="India"
)

# User: Shahwar
# Message: Hello!
# Urgent: True
# Extra data: {'timestamp': '10:30 AM', 'location': 'India'}