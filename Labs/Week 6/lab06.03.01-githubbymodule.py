from github import Github
# remove the minus sign from the key
g = Github("c7adca01d62fd0d9a8bbd07e88724a708a06b17f")
for repo in g.get_user().get_repos():
 print(repo.name)