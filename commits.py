import requests


def get_user_info():
    URL = "https://api.github.com/repos/realaltffour/GraphSolver/contributors"
    r = requests.get(URL)
    r = r.json()

    for contributor in r:
        get_user_commits(contributor['login'], contributor['url'])

def get_user_commits(login, github_profile):
    URL = "https://api.github.com/repos/realaltffour/GraphSolver/commits"
    # Filter by login
    r = requests.get(URL, {'author':login})
    r = r.json()
    
    with open('CONTRIBUTORS.md', 'a') as contributor_file:
        contributor_file.write(f"\n{login} {github_profile}\n")
        for commits_by_user in r:
            commit_sha = commits_by_user['html_url'].split('/')[-1][:7]
            contributor_file.write(f"* [{commit_sha}]({commits_by_user['html_url']})\n")

    contributor_file.close()

get_user_info()
