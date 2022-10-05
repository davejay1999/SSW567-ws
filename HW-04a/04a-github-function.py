import unittest
import requests
import json

def GithubApi(username):
    try:
        try:
            githubResponse = requests.get("https://api.github.com/users/" + username + "/repos")
            if githubResponse.status_code != 200:
                return "GitHub User doesn't exist!!"

        except Exception as e:
            return "GitHub User doesn't exist!!"

        githubResponse = githubResponse.json()

        if len(githubResponse) == 0:
            return "No Repos"

        for repository in githubResponse:
            repoResponse = requests.get(repository['commits_url'].split("{")[0])
            repoResponse = repoResponse.json()
            print("Repo: "+ repository['name'] + " Number of commits: " + str(len(repoResponse)))
    
        return "success"

    except Exception as e:
        return ("ERROR:-", e)

# DEMO TESTING 
class TestRepoAPI(unittest.TestCase):
    def testUserNotExist(self):
        self.assertEqual(GithubApi('XXXYYYZZZ111222333'), "GitHub User doesn't exist!!")
    def testUserSuccess(self):
        self.assertEqual(GithubApi('davejay1999'), "success")


if __name__ == "__main__":
    userInput = input("Enter Github Username: ")
    message = GithubApi(userInput)
    print(message)
    print('DEMO TestCase')
    unittest.main()




# ---------------------------------------------------------X------------------------------------------------
















