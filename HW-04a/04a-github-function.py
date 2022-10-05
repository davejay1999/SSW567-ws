#!/usr/bin/env python3
# It will help reader,informing that code is in python3.
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
__author__ = "JAY DAVE"
__contact__ = "jdave1@stevens.edu"
__date__ = "2022/10/05"
__license__ = "XYZ"
__maintainer__ = "JAY DAVE"
__version__ = "1.0.0"
# ---------------------------------------------------------------------------

"""
AIM of SCRIPT:
For this assignment imagine that you have been asked to develop a function that will interface with GitHub in order to extract and present useful information to your user. 
The function will communicate using the RESTful services APIs provided by GitHub. The GitHub APIs will allow you to query for information about users, repositories, etc... 
which can be retrieved using the function, and then be displayed in the application.


NOTE:- If you make too many API requests of GitHub then you may reach a limit and then GitHub will start to give errors.
You can only perform so many tests of GitHub APIs within some period of time, so realize that if your tests are passing fine and then all of a sudden they start to fail, 
then it may be because you have exceeded the limits on GitHub.
You will need to stop testing and wait for a period of time before GitHub will allow further requests.
"""

import unittest
import requests
import json

def GithubApi(username):
    try:
        try:
            githubResponse = requests.get("https://api.github.com/users/" + username + "/repos")
            # if failed response from github return user not exist message.
            if githubResponse.status_code != 200:
                return "GitHub User doesn't exist!!"

        except Exception as e:
            return "GitHub User doesn't exist!!"

        githubResponse = githubResponse.json()
        # if no public repos then return No repos message.
        if len(githubResponse) == 0:
            return "No Repos"

        # loop to fetch all public repos and then count number of commits repos have.
        for repository in githubResponse:
            repoResponse = requests.get(repository['commits_url'].split("{")[0])
            repoResponse = repoResponse.json()
            print("Repo: "+ repository['name'] + " Number of commits: " + str(len(repoResponse)))

        return "success"

    except Exception as e:
        return ("ERROR:-", e)

# DEMO TESTING 
class TestRepoAPI(unittest.TestCase):
    # testcase when user is not exist.
    def testUserNotExist(self):
        self.assertEqual(GithubApi('XXXYYYZZZ111222333'), "GitHub User doesn't exist!!")
    # testing success message by calling my username.
    def testUserSuccess(self):
        self.assertEqual(GithubApi('davejay1999'), "success")


if __name__ == "__main__":
    userInput = input("Enter Github Username: ")
    message = GithubApi(userInput)
    print(message)
    print('DEMO TestCases')
    unittest.main()




# ---------------------------------------------------------X------------------------------------------------
















