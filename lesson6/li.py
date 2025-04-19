import requests

# This script demonstrates a simple example of interacting with the Roblox API using Python.
# Note: Roblox APIs often require authentication and specific endpoints. 
# Make sure to check the official Roblox documentation for details.


# Example: Fetching details of a Roblox user by username
def get_user_info(username):
    url = f"https://users.roblox.com/v1/usernames/users"
    payload = {"usernames": [username]}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        if data["data"]:
            return data["data"][0]
        else:
            return "User not found."
    else:
        return f"Error: {response.status_code}"

# Example usage
if __name__ == "__main__":
    username = input("Enter Roblox username: ")
    user_info = get_user_info(username)
    print(user_info)