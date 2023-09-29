def UsefulLinks():
  #printing the different links that the user can choose from
  print("Useful Links:\n1) General\n2) Browse InCollege\n3) Business Solutions\n4) Directories\n5) Go back to the previous page")
  choice = input("Please enter the number for your preferred choice: ")

if choice == 1:
  def DsiplayGeneral():
    #need to add the sign up option
    print("1) Help Center\n2) About\n3) Press\n4) Blog\n5) Careers\n6) Developers")
    option = input("Please enter the number for your preferred choice: \n")
    if option == 1:
      print("We're here to help")
    elif option == 2:
      print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
    elif option == 3:
      print("In College Pressroom: Stay on top of the latest news, updates, and reports")
    elif option == 4:
      print("Under construction")
    elif option == 5:
      print("Under construction")
    elif option == 6:
      print("Under construction")
elif choice == 2:
  print("Under construction")
elif choice == 3:
  print("Under construction")
elif choice == 4:
  print("Under construction")
else:
  while(1 > choice > 4):
    input("Invalid Choice. Please enter a number between 1 and 4: ")
    
