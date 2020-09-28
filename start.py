import requests


def get_repo_names_by_id(id):
    response = requests.get("https://api.github.com/users/{}/repos".format(id)).json()
    print(response)
    return list(map(lambda x: x["name"], response))


def get_commites(id, repoName):
    return len(requests.get("https://api.github.com/repos/{}/{}/commits".format(id, repoName)).json())


if __name__ == "__main__":
    repoNames = get_repo_names_by_id("IncapableFury")
    for repoName in repoNames:
        commits = get_commites("IncapableFury", repoName)
        print('Repo: {:20} Number of commits: {}'.format(repoName, commits))

    # ---------fancy but nonsensical one-liner warning---------
    # print(*list(map(lambda repo: 'Repo: {:20} Number of commits: {}'.format(repo["name"], len(
    #     requests.get("https://api.github.com/repos/IncapableFury/{}/commits".format(repo["name"])).json())),
    #                 requests.get("https://api.github.com/users/IncapableFury/repos").json())), sep='\n')
