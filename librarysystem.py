import random
#Library Management System
print("Welcome to the library")

#Making special symbols list for validating special symbols of password
specialchar_list = ["@", "^", "*", "%", "<", ",", "~" ]
#Making numbers list for validating numbers of password
numbers_list = [0,1,2,3,4,5,6,7,8,9]
#Making list of codes for the users library id 
library_id = []
for i in range (100, 1000):
    library_id.append(i)
ids = random.choice(library_id)
library_id.remove(ids)


#Making login and signup for the user to increase security 
class Userinfo_signup():
    def __init__(self, username, password, location_info,):
        self.username = username
        self.password = password
        self.location_info = location_info

class Userinfo_login():
    def __init__(self, username_login, password_login, library_id_login ):
        self.username_login = username_login
        self.password_login = password_login
        self.library_id_login = library_id_login

#Selecting for signup or login by the user
user = input("Signup/Login:").lower()

#Signup
database_user = []
def Signup():
    while True:
        username = input("Enter your username: ").lower()
        if username == "":
            print("Username must not be empty")
            continue
        if username in database_user:
            print("Username already exists")
            continue
        while True:
            password = input("Create your password: ")
            if len(password) < 8:
                print("Password must be 8 characters minimum")
                continue
            if not any(char in specialchar_list for char in password):
                print("Password must contain special symbols")
            else:
                break
        location_info = input("Enter your location info: ").lower()
        if location_info == "":
            continue

        signup_info = Userinfo_signup(username, password, location_info)
        database_user.append(signup_info)
        print("Signup Succesfull")
        print(f"Your new Library ID is {ids}, use it for your login")
        print("Thank You")
        with open("/home/mehr-ali/Documents/Projects Python/usersinfo.txt", "a") as file:
            file.write(f"{signup_info.username},{signup_info.password},{signup_info.location_info},{ids} \n")
        break
if user == "signup":
    Signup()



