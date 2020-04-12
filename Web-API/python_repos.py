import requests

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r=requests.get(url)
print('Status Code:',r.status_code)

# Store API response in a variable.
response_dict=r.json()
print("Total repositories:",response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned:",len(repo_dicts))

# Examine the first repository
