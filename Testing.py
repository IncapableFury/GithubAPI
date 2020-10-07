import unittest
from unittest import mock
import start
import mockdata  # a copy of the actual response


def mocked_requests_get(url):
    class MockResponse:
        def __init__(self, mockurl):
            self.mockurl = mockurl

        def json(self):
            return self.pick_commit(self.mockurl)

        def pick_commit(self, url):
            if url == "https://api.github.com/repos/IncapableFury/Triangle_Testing/commits":
                return mockdata.Triangle_Testing_commits
            elif url == "https://api.github.com/repos/IncapableFury/CS-546/commits":
                return mockdata.CS546_commits

    return MockResponse(url)


class TestGithubAPI(unittest.TestCase):

    @mock.patch("requests.get")
    def testRepoGetter(self, mock_get):
        mock_get.return_value.json.return_value = mockdata.repos
        assert start.get_repo_names_by_id("IncapableFury") == ['CS-546', 'CS-554', 'CS546_FinalProject-1',
                                                               'Final_Project_SW555', 'GithubAPI',
                                                               'HomeWorks_For_EE552',
                                                               'Triangle_Testing']

    @mock.patch("requests.get")
    def testCommitGetter(self, mock_get):
        mock_get.side_effect = mocked_requests_get
        assert start.get_commits("IncapableFury", "CS-546") == 30
        assert start.get_commits("IncapableFury", "Triangle_Testing") == 13


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
