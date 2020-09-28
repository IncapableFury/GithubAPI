import unittest
from start import *


class TestGithubAPI(unittest.TestCase):
    def testRepoGetter(self):
        assert get_repo_names_by_id("IncapableFury") == ["CS-546", "CS-554", "CS546_FinalProject-1", "Final_Project_SW555",
                                                   "GithubAPI", "HomeWorks_For_EE552", "Triangle_Testing"]

    def testCommitGetter(self):
        assert get_commites("IncapableFury", "CS-546") == 30
        assert get_commites("IncapableFury", "Triangle_Testing") == 10


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
