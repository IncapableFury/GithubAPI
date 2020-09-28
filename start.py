import requests

if __name__ == "__main__":
    # r = requests.get("https://api.github.com/users/IncapableFury/repos").json()
    # for repo in r:
    #     # repoName = repo["name"]
    #     # c = requests.get("https://api.github.com/repos/IncapableFury/{}/commits".format(repoName)).json()
    #     print('Repo: {:20} Number of commits: {}'.format(repo["name"], len(
    #         requests.get("https://api.github.com/repos/IncapableFury/{}/commits".format(repo["name"])).json())))

    # ---------fancy but nonsensical one-liner warning---------
    print(*list(map(lambda repo: 'Repo: {:20} Number of commits: {}'.format(repo["name"], len(
        requests.get("https://api.github.com/repos/IncapableFury/{}/commits".format(repo["name"])).json())),
                        requests.get("https://api.github.com/users/IncapableFury/repos").json())), sep='\n')
