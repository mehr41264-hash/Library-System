import random
#Library Management System
print("Welcome to the library")
#Root user who can only add books
def root_user():
    while True:
        admin = input("Enter your username: ")
        if admin != "admin":
            print("Wrong credentials")
            continue
        break
    while True:
        password = input("Enter your password: ")
        if password != "mehr@li123":
            print("Wrong Password")
            continue

        print("Login Successful")
        break
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

#Addind books to the library class
available_books = []
class AddBooks():
    def add_book(self, book, author):
        self.book = book
        self.author = author
        available_books.append((self.book, self.author))
        print(f"The new book which  was added is {self.book} written by {self.author}")
        
        with open("/home/mehr-ali/Documents/Projects Python/availablebooks.txt", "a") as file:
            file.write(f"{self.book},{self.author} \n")

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
user = input("Signup /Login / AddBooks: ").lower().strip()

#Signup
database_user = []
record = None
with open("/home/mehr-ali/Documents/Projects Python/usersinfo.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            database_user.append(line.split(","))
def Signup():
    while True:
        username = input("Enter your username: ").lower()
        if username == "":
            print("Username must not be empty")
            continue
        for record in database_user:
            if record[0] == username:
                print("Username already exists, Try making a new one")
                continue
                break
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
        print(f"Your new Library ID is {int(ids)}, use it for your login")
        print("Thank You")
        with open("/home/mehr-ali/Documents/Projects Python/usersinfo.txt", "a") as file:
            file.write(f"{signup_info.username},{signup_info.password},{signup_info.location_info},{ids} \n")
        break
if user == "signup":
    Signup()

#Login 
database_user = []
with open("/home/mehr-ali/Documents/Projects Python/usersinfo.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            database_user.append(line.split(","))
def Login():
    while True:
        username_login = input("Enter your username: ").lower()
        if username_login == "":
            print("Username can't be empty")
            continue
        user_record = None
        for record in database_user:
            if record[0] == username_login:
                user_record = record
                break
        password_login = input("Enter your password: ")
        if user_record[1] != password_login:
            print("Wrong Password Entered")
            continue
        library_id_login = int(input("Enter your Library id: "))
        if int(user_record[3]) != library_id_login:
            print("Wrong Library ID")
            continue
        if library_id_login == "":
            print("Library ID must not be empty")
            continue
        break

    login_info = Userinfo_login(username_login, password_login, library_id_login)
    print("Login Successful!!")

if user == "login":
    Login()
#Function for the inputs
def adding_boooks():
    book = input("Enter the name of the book: ")
    author = input("Enter the name of the author: ")
    added_books = AddBooks()
    added_books.book = book
    added_books.author = author
    added_books.add_book(book, author)
#AddBooks
if user == ("addbooks"):
    root_user()
    adding_boooks()