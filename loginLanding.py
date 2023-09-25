from database import *
import time
#intialize a stack to navigate through the program 
#navigation_stack = []

def userHome():
    from landing import startupLanding
  
    loopBreaker = True 
    while loopBreaker:
        print("\nWelcome User!")
        print("Please select the number of the service you would like to use:")
        print("Search for a job / internship (1)")
        print("Find someone that they know (2)")
        print("Learn a new skill (3)")
        print("Return to previous page (4)")
    
        option = int(input("Please select your option: ")) 
      
        if option == 1:
          searchForJob()
        elif option == 2:
          findSomeoneTheyKnow()
        elif option == 3:
          learnASkill()
        elif option == 4:
          startupLanding()
          #print("returning to previous page")
          #return navigation_stack.pop()  
        else:
            print("Invalid input. Exiting program")
        yesNo = input("Would you like to continue (yes/no): ")
        if yesNo.lower() == "yes":
            continue
        else:
            loopBreaker = False
            return

# Option functions to fill out once we understand what we need to do for them 
def searchForJob():
    #print("Searching for a job is under construction")
    print("\nWelcome to Job Search!\n1) post a job\n2) go back to the previous page")
    choice = int(input("Please select an option: "))
  
    if(choice == 1):
      print("\nEnter the following information about the job: ")
      title = input("Enter the job title: ")
      description = input("Enter the job description: ")
      employer = input("Enter the employer: ")
      location = input("Enter the location: ")
      salary = input("Enter the job's salary: ")
      firstname = input("Enter your first name: ")
      lastname = input("Enter your last name: ")

      storeJob(title, description, employer, location, salary, firstname, lastname)

      
    elif(choice == 2):
      print("returning to job search")
      userHome()
    else:
      while(choice!= 1 and choice != 2):
        print("invalid input")
        print("1) post a job\n2) go back to the previous page")
        choice = input("Please select an option: ")

  
def learnASkill():
    loopBreaker1 = True
    while loopBreaker1:
        print("\nPlease select any of following skills:")
        print("1. Web Development ")
        print("2. Leadership ")
        print("3. Time management ")
        print("4. Data Literacy ")
        print("5. Interview Prep ")
        print("6. Return to Welcome Screen ")
        UserOption = int(input("Please select your option: ")) 
        if UserOption == 1:
            print("Web Development is under construction")
        elif UserOption == 2:
            print("Leadership is under construction")
        elif UserOption == 3:
            print("Time management is under construction")
        elif UserOption == 4:
            print("Data literacy is under construction")
        elif UserOption == 5:
            print("Interview prep is under construction")
        elif UserOption == 6:
            userHome()
        else:
            print("Invalid input.")
            
        cont = input("Would you like to continue (yes/no): ")
        if cont.lower() == "yes":
            continue
        elif cont.lower()!="yes":
            loopBreaker1=False
            exit(0)


def storeJob(title, description, employer, location, salary, firstName, lastName):
  cursor.execute("SELECT COUNT(*) FROM jobs")
  job_count = cursor.fetchone()[0]

  if job_count >= MAX_ACCOUNTS:
    print("All permitted jobs have been created. Please come back later.")
    userHome()

  cursor.execute("INSERT INTO jobs (title, description, employer, location, salary, firstname, lastname) VALUES (?, ?, ?, ?, ?, ?, ?)", (title, description, employer, location, salary, firstName, lastName))
  
  conn.commit()
  print("Job stored in database")
  userHome()


def findSomeoneTheyKnow():
    firstname = input("\nEnter a first name to search: ")
    lastname = input("Enter a last name: ")
    
    cursor.execute("SELECT * FROM users WHERE firstName=? AND lastName=?",(firstname, lastname))
    user = cursor.fetchone()
    
    loopBreaker = True
    loopBreak = True
  
    if user:
        while loopBreaker:
            print("They are a part of the InCollege system")
            print("Username: " + user[0])
            print("First Name: "  + user[2])
            print("Last Name: " + user[3])
        
            loopBreaker = False
            time.sleep(3)
            userHome()
    
    else:
        print("They are not yet a part ofthe InCollege system yet")  
        while loopBreak:
            uInput = input("Enter 1 to return to main menu: ")
            if uInput == "1":
                loopBreak = False
                userHome()
            else:
                uInput = input("Enter 1 to return to main menu please: ")
                userHome()

