import requests
 
def get_mother_id(username):
    url = f"https://discord.com/api/v9/users/{username}/relationships?limit=1&relationship=mother"
    response = requests.get(url)
    data = response.json()
 
    if data["members"]:
        mother_id = data["members"][0]["id"]
        return mother_id
    else:
        return "No mother found"
 
def main():
    username = input("Enter the Discord username: ")
    mother_id = get_mother_id(username)
    print(f"The mother's ID is: {mother_id}")
 
if __name__ == "__main__":
    main()
