import requests
 
def get_user_data(username):
    url = f"https://discord.com/api/v9/users/{username}/"
    response = requests.get(url)
    data = response.json()
    return data
 
def get_user_friends(username):
    url = f"https://discord.com/api/v9/users/{username}/friends?limit=100"
    response = requests.get(url)
    data = response.json()
    return data["data"]
 
def get_user_email(username):
    user_data = get_user_data(username)
    if "email" in user_data:
        return user_data["email"]
    else:
        return None
 
def main():
    username = input("Enter the username: ")
    email = get_user_email(username)
    friends = get_user_friends(username)
    print(f"Email: {email}")
    print(f"Friends: {friends}")
 
if __name__ == "__main__":
    main()
