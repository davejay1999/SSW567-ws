Week 2:  Assignment 02a

NOTE:  you should do this assignment (02a) before you attempt assignment (02b)

The objective of this assignment is for you to (a) develop a set of tests for an existing triangle classification program, (b) use those tests to find and fix defects in that program, and (c) report on your testing results for the Triangle problem

Description of assignment:

Sometimes you will be given a program that someone else has written, and you will be asked to fix, update and enhance that program.   In this assignment you will start with an existing implementation of the classify triangle program that will be given to you.   You will also be given a starter test program that tests the classify triangle program, but those tests are not complete.  

    These are the two files:  Triangle.py and TestTriangle.py
        Triangle.py is a starter implementation of the triangle classification program.  
        TestTriangle.py  contains a starter set of unittest test cases to test the classifyTriangle() function in the file Triangle.py file.   

In order to determine if the program is correctly implemented, you will need to update the set of test cases in the test program.  You will need to update the test program until you feel that your tests adequately test all of the conditions.   Then you should run the complete set of tests against the original triangle program to see how correct the triangle program is.    Capture and then report on those results in a formal test report described below.   For this first part you should not make any changes to the classify triangle program.  You should only change the test program.

Based on the results of your initial tests, you will then update the classify triangle program to fix all defects.  Continue to run the test cases as you fix defects until all of the defects have been fixed.   Run one final execution of the test program and capture and then report on those results in a formal test report described below.   

Note that you should NOT simply replace the logic with your logic from Assignment 1.  Test teams typically don't have the luxury of rewriting code from scratch and instead must fix what's delivered to the test team.   

 Triangle.py contains an implementation of the classifyTriangle() function with a few bugs.  

TestTriangle.py contains the initial set of test cases

 

Part 0:

Create a new folder under your GitHub repository for SSW567 that you have created and shared with the instructor and TA.   When creating the new folder, you should include a README file under it.   Give your new folder a meaningful name.   In our example here we will name our folder for this homework as "hw-02a" but you can name it anything (as long as it makes sense for this assignment).   

 

 

Of course, you should have git installed on your laptop, but if you do not then you will need to do that first.  You can download git from here:  https://git-scm.com/downloads (Links to an external site.) 

Next you should upload and commit both of these files, Triangle.py and TestTriangle.py in their original form to the new folder in your GitHub repo   Then any changes you make to these programs will also be committed to the same GitHub repo.

Here are the steps to do this:

    copy your two Triangle source files to your local repository folder,
    then add and commit them to git, and t
    hen push those files up to your repository on GitHub.

a. Copy Triangle.py and TestTriangle.py to the Triangle567 folder.     

b. Next you should run these commands to add and commit the changes to your local repository on your laptop:

$ git add TestTriangle.py Triangle.py 
$ git commit -m "add triangle code"

c. Finally, you should run this command to push the changes to GitHub:

$ git push

 

 

Part 1:

    Review the Triangle.py file which includes the classifyTriangle() function implemented in Python.  
    Enhance the set of test cases for the Triangle problem that adequately tests the classifyTriangle() function to find problems.  The test cases will be in a separate test program file called TestTriangle.py .  You should not fix any bugs in Triangle.py at this time, just make changes to TestTriangle.py
    Run your test set against the classifyTriangle() function by running:
        python -m unittest TestTriangle
    Create a test report in the format specified below.  This report shows the results of testing the initial classifyTriangle() implementation.
    Commit and push your changes to the TestTriangle.py program to GitHub

Part 2:

    After you've completed part 1 that defines your test set and after running it against the buggy classifyTriangle() function, update the logic in classifytTriangle() to fix all of the logic bugs you found by code inspection and with your test cases.
    Run the same test set on your improved classifyTriangle() function and create a test report on your improved logic
    Commit and push your changes to the Triangle.py program to GitHub

 

Deliverables:

1. Include a written test report in your assignment summary with the results of running your test set against the initial buggy implementation of classifyTriangle in the origianl Triangle.py using  the following format:

 
Test ID 	Input 	Expected Results 	Actual Result 	Pass or Fail
  	  	  	  	 
  	  	  	  	 
  	  	  	  	 
  	  	  	  	

 

 

 

2. Upload a copy of your source code for your improved classifyTriangle  (file named Triangle.py)

3. Upload a copy of your test set.  Your test set should be in a separate file (file named TestTriangle.py)

4. Upload a screen dump or output file of running your test set on the improved classifyTriangle() function

5. Include a written test report in your assignment summary with the results of running your test set against the improved implementation of classifyTriangle using  the following format:

 
Test ID 	Input 	Expected Results 	Actual Result 	Pass or Fail
  	  	  	  	 
  	  	  	  	 
  	  	  	  	 
  	  	  	  	

 

 

 

6.  Your assignment summary should include a matrix as shown below in the summary results along with a description of the strategy you used to decide when you had a sufficient number of test cases. 

 

 

 

 
	

Test Run 1

 

 
	

Test Run2

 

 
	

….

 

 

Tests Planned

 

 
	

 

 

 
	

 

 

 
	

 

 

 

Tests Executed

 

 
	

 

 

 
	

 

 

 
	

 

 

 

Tests Passed

 

 
	

 

 

 
	

 

 

 
	

 

 

 

Defects Found

 

 
	

 

 

 
	

 

 

 
	

 

 

 

Defects Fixed

 

 
	

 

 

 
	

 

 

 
	

 

 

 

 

7. Submit the name of the repo containing all of the code for this assignment

All assignments should be written up in the following format:

All project reports should include the following standard information in the following order:

1. Assignment Description: write it out! (cut and paste is fine)

2. Author: Your name

3. Summary: at the top, include

- a summary of your results

- reflection -- this is where you actually think about the assignment after it is over -- what did you learn? What worked, what didn't?

5. Honor pledge

6. Detailed results, if any:

- A careful description of techniques you used (In this case, this item may not apply)

- Details of any assumptions or constraints made

- A description of whatever data inputs you used

- An explanation of the results of your work. In this case, upload copies of the code, the sanity tests, and the results,  plus any other relevant results about the tools selection/installation/usage.

 

 
Submission
Submitted!
Sep 21 at 9:45pm
Submission Details
Download hw_02a triangle_testing.docx
Comments:
https://github.com/davejay1999/SSW567-ws We can find ClassifyTriangle and TestTriangle files in GitHub
Jay Jignesh Dave, Sep 21 at 9:45pm
