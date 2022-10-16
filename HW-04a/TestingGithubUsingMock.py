import unittest
import unittest.mock
from unittest.mock import patch


# using both mock methods.
# 1. by using decorators.
# 2. by using with statement



mocking_github_response = """
Repo: Bus-Reservation-system-DBMS Number of commits: 1
Repo: davejay1999 Number of commits: 2
Repo: Dbms Number of commits: 2
Repo: django-phonenumber-field Number of commits: 30
Repo: first Number of commits: 1
Repo: GitHubApi567 Number of commits: 16
Repo: OS-page-scheduling-methods Number of commits: 2
Repo: OS_page_replacement_simulator Number of commits: 2
Repo: post_crud_token_based Number of commits: 7
Repo: SSW567-ws Number of commits: 26
Repo: UMD-course-projects Number of commits: 30
Repo: wigme-wiki Number of commits: 2
"""




class TestRepoAPI(unittest.TestCase):

    # testcase when user is not exist.
    @patch("githubfunction.GithubApi")
    def testUserNotExist1(self,MockingGithubApi):
        MockingGithubApi.return_value = "GitHub User doesn't exist!!"
        self.assertEqual(MockingGithubApi('XXXYYYZZZ111222333'), "GitHub User doesn't exist!!")


    # testcase when user is not exist.
    def testUserNotExist2(self):
        with patch('githubfunction.GithubApi') as MockingGithubApi:
            MockingGithubApi.return_value = "GitHub User doesn't exist!!"
            self.assertEqual(MockingGithubApi('XXXYYYZZZ111222333'), "GitHub User doesn't exist!!")
    
    # testing success message by calling my username.
    @patch("githubfunction.GithubApi")
    def testUserExist1(self,MockingGithubApi):
        MockingGithubApi.return_value = mocking_github_response
        self.assertEqual(MockingGithubApi('davejay1999'), mocking_github_response)

    # testing success message by calling my username.
    def testUserExist2(self):
        with patch('githubfunction.GithubApi') as MockingGithubApi:
            MockingGithubApi.return_value = mocking_github_response
            self.assertEqual(MockingGithubApi('davejay1999'), mocking_github_response)

if __name__ == "__main__":
    unittest.main()
