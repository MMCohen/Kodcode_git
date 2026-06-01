import requests

post_rsp = requests.get("https://jsonplaceholder.typicode.com/posts")
users_rsp = requests.get("https://jsonplaceholder.typicode.com/users")

post_data = post_rsp.json()
users_data = users_rsp.json()

users_dict = {user["id"]: user["name"] for user in users_data}
# print(users_dict)

for post in post_data:
    print(f"{post['title']} | by: {users_dict[post['userId']]}")