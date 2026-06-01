import requests

# response = requests.get(" https://jsonplaceholder.typicode.com/users/1")
#
# data = response.json()
#
# name = data["name"]
# email = data["email"]
# city = data["address"]["city"]
#
# print(f"{name = }\n{email = }\n{city = }")
#
# posts = requests.get("https://jsonplaceholder.typicode.com/posts")
#
# posts_data = posts.json()
#
# print(f"total posts: {len(posts_data)}")

posts = requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")
data = posts.json()

for user in data:
    print(f" - {user['title']}")




