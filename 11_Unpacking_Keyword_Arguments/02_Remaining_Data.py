def my_post(url, data=None, json=None, **kwargs):
    print("URL:", url)
    print("Data:", data)
    print("JSON:", json)
    print("Other:", kwargs)


# Example call
my_post(
    "https://api.example.com",
    data={"name": "Shahwar"},
    headers={"Authorization": "Bearer token"},
    timeout=5
)

# URL: https://api.example.com
# Data: {'name': 'Shahwar'}
# JSON: None
# Other: {'headers': {'Authorization': 'Bearer token'}, 'timeout': 5}