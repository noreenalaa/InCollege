from UserCreateLogin import *
from userStories import *

import os
import random

#Note: Video function is in userStories file

def clear_screen():
  os.system('clear')

random_number = random.randint(0, 2)
  
def startupLanding():
    clear_screen()
    # Comment this code chunk out before submission
    cursor.execute("SELECT username, password, firstName, lastName FROM users")
    user_data = cursor.fetchall()
    if user_data:
        print("*** testing data only ***")
        print("Saved User Information:")
        for row in user_data:
            print("Username:", row[0], "/ Password:", row[1], " / First Name:", row[2], "/ Last Name:", row[3])

    cursor.execute("SELECT title, description, employer, location, salary, firstname, lastname FROM jobs")
    job_data = cursor.fetchall()
    if job_data:
      print("Saved Jobs Information:")
      for row in job_data:
        print("Title:", row[0], "/ Description:", row[1], " / Employer:", row[2], "/ Location:", row[3], "/ Salary:", row[4], "/ FirstName:", row[5], "/LastName:", row[6])
    print("*** end of testing data ***\n")
    # Up to this point needs to be commented out before submission
  
    #User stories
    cursor.execute("SELECT story FROM stories")
    userStory = cursor.fetchall()
  
    print("User Stories: ")
    print(userStory[random_number])
    print("\n")
  
    # User menu
    print("Welcome to inCollege: inCollege is your")
    print("Login: (1)")
    print("Sign up: (2) ")
    print("Delete Users: (3)")
    print("Look up a user: (4)")
    print("Watch Video: (5)")

    uInput = int(input("Please select either 1, 2, 3, 4, or 5 based on which option you would like to do: "))

    # Once option is picked we then will choose which function that needs to be done
    if uInput == 1:
        UserLogin()
    elif uInput == 2:
        createUser()
    elif uInput == 3:
        deleteUser()
    elif uInput == 4:
        searchUser()
    elif uInput == 5:
      videoPlay()
    else:
        print("Invalid option")