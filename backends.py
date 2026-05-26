from flask import flask, jsonify
from flask_cors import CORS
import sqlite3
import time 
    
print("==================Sign_up your account======================")
firstname = input("Enter your fristname:    ").title().strip()
lastname = input("Enter your lastname:    ").title().strip()
email = input("Enter your email:    ").lower().strip()
password = input("Enter your password:  ").strip()


while True:
   
    error = []
    if len(password) < 8:
        error.append("Password must be at least 8 characters long")
    if not any(char.isdigit() for char in password):
        error.append("Password must contain at least one digit")
    if not any(char.isupper() for char in password):
        error.append("Password must contain at least one uppercase letter")
    if not any(char.islower() for char in password):
        error.append("Password must contain at least one lowercase letter")
    if not any(char in "!@#$%^&*()_+-=[]{}|;':\"<>,./?" for char in password):
        error.append("Password must contain at least one special character")
        
    if error:
        for err in error:
            print(err)
        password = input("Enter new password:  ").strip()
    else:
        break
account = {
    "firstname": firstname,
    "lastname": lastname,
    "email": email,
    "password": password,
    "locked_until": None
}
    
print(f"Welcome {firstname} {lastname}")
print(f"your email is {email}")
print("Your account has been created successfully")
print()

print("============== login to your account ===============")
login_attempt = 3
logout_duration = 30



while login_attempt > 0:
    login_email = input("Enter your email:    ").lower().strip()
    login_password = input("Enter your password:  ").strip()

    
    if login_email == email and login_password == password:
        print("Login successful")
        break
    else:    
        print("Login failed")
        login_attempt -= 1
        if login_attempt > 0:
            print("Wrong email or password")
            print(f"You have {login_attempt} left")
        else:
            print("Account has been locked")
            break

