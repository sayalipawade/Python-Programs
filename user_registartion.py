import re

class UserRegistration:

    #constants
    valid_name_pattern='^[A-Z]([a-zA-Z]{2,})$'
    valid_mobile_pattern='^[0-9]{2}[0-9]{10}$'
    valid_email_pattern='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    valid_password_pattern="^(?=.*[0-9])"+"(?=.*[a-z])(?=.*[A-Z])"+"(?=.*[@#$%^&+=])"+"(?=\\S+$).{8,20}$"

    #Checking First name is valid or not
    def first_name_checking(self):
        first_name=(input("Enter first name:"))
        match=re.match(self.valid_name_pattern,first_name)
        if match:
            print("First name is valid")
        else:
            print("First name is Invalid")

    #Checking Last name is valid or not
    def last_name_checking(self):
        last_name=(input("Enter last name:"))
        match=re.match(self.valid_name_pattern,last_name)
        if match:
            print("Last name is valid")
        else:
            print("Last name is Invalid")

    #Checking Mobile no is valid or not
    def mobile_number_checking(self):
        mobile_number=(input("Enter mobile no:"))
        match=re.match(self.valid_mobile_pattern,mobile_number)
        if match:
            print("Mobile no is valid")
        else:
            print("Mobile no is Invalid")

    #Checking Email is valid or not
    def email_checking(self):
        global email
        email=input("Enter Email:")
        match=re.match(self.valid_email_pattern,email)
        if match:
            print("Email is valid")
        else:
            print("Email is not valid")

    def password_checking(self):
        global password
        password=input("Enter Password:")
        match=re.match(self.valid_password_pattern,password)
        if match:
            print("Password is valid")
        else:
            print("Password is not valid")

user=UserRegistration()
user.first_name_checking()
user.last_name_checking()
user.mobile_number_checking()
user.email_checking()
user.password_checking()
