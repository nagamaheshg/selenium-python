# password = input("Enter your password")
# score = float(input("Enter your Score: "))

# if password == "Admin@123":
    
#     print("Display Dash board")

# else:
#     print("Invalid Credentials")
    

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print(f"Your grade is: {grade}")

user_name = input("Enter user name")
password = input("Enter password")

if user_name == 'Admin' and password == "Admin@123":
    
    print("Login successfully!")
    
else:
    print("Please check you credentials!")


browser = input("Enter browser name to test: ")

if browser == 'chrome' or browser == 'Firefox':
    print(f"your choose {browser}. It supported for testing")

else: 
    print("It will not support for our testing")
    

user_type = input("Enter user type")
status = bool(input("Enter your status"))

if user_type == 'Admin':
    
    if status: # False, '', None, [], {}        
        print("Admin")
    
    else:
        print("You're not active")
        
else:
    print("Invalid user")