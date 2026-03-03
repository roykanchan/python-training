import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

output = response.json()

for item in range(len(output)):
    print(output[item]["user"]["login"])

#OR

# for item in output:
#     users = item["user"]["login"]
#     print(users)