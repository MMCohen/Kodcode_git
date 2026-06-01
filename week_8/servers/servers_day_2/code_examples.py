import requests
import uvicorn
from fastapi import FastAPI


# # Example 1
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1", {"try":"hello world"})
#
#
# print(response.status_code)
# print(response.json())
# print(response.text)
#
# data = response.json()
# print(data["body"])


# # Example 2
#
# new_post = {
# "title": "My First Post",
# "body": "This is the content",
# "userId": 1
# }
#
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post)
# print(response.status_code)
# print(response.json())


# # Example 3
# updated = {"id": 1, "title": "New Title", "body": "New content", "userId": 1}
# r = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated)
# print(r.status_code)
# r = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
# print(r.status_code)


# # Example 4
# params = {"userId": 4}
# response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)
#
# posts = response.json()
# print(f"Found {len(posts)} posts for user 1")
#
# for post in posts[:3]:
#     print(f" - {post['title']}")


# # Example 5
# app = FastAPI()
#
# @app.get("/users")
# def get_users(role: str = "all", page: int = 1):
# # Called as: GET /users?role=admin&page=2
#     return {"role": role, "page": page, "users": []}
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1",port=8000)



# # Example 6
# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# if response.status_code == 200:
#     print("Got data:", response.json())
# elif response.status_code == 404:
#     print("Not found")
# else:
#     print(f"Unexpected status: {response.status_code}")


# # Example 7



