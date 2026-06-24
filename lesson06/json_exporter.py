import json
user = '{"name":"Vlad","python":"Beginner"}'
user1 = json.loads(user)
print(user1["python"])