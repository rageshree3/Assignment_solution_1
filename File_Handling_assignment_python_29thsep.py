#!/usr/bin/env python
# coding: utf-8

# #TASK_1
# 
# Read the text file and capture the password from file.
# Ask user to input password.
# If password is correct than open google chrome for user to access internet.
# Else says permission denied.

# This code will work if there is only one password in the file

# In[22]:


import webbrowser

#Read the password from the file
with open('password.txt', 'r') as file:
    saved_password = file.read()

#Ask user to enter the password
user_password = input("Please enter your password: ")

#Check if the password is correct
if user_password == saved_password:
    print("Password is correct. Opening Google Chrome...")
    webbrowser.open('https://www.google.com')
else:
    print("permission denied")


# 

# This code will work if there is more than 1 password. It will open the browser if any of the password matches with the one the user entered

# In[23]:


import webbrowser

#Read the passwords from the file
with open('password_1.txt', 'r') as file:
    saved_passwords_1 = file.read()

#Ask the user to enter the password
user_password_1 = input("Please enter your password: ")

#Check if the entered password is in the list of saved passwords
if user_password_1 in saved_passwords_1:
    print("Password is correct. Opening Google Chrome...")
    webbrowser.open('https://www.google.com')  
else:
    print("permission denied")


# In[ ]:





# In[ ]:





# #Task_2
# 
# create 2 files:
# 1.username_file.txt : where user will create his username_file.txt and write username in this file.
# 2.userpassword_file.txt : Where user will create userpassword_file.txt and write his password in this
# fie.
# 
# now user will login through the username and password:
# you will read both files username_file.txt and userpassword_file.txt
# 
# you will check both the input correct entered by the user.
# If both details are correct than you will open google.com for surfing
# else print message permission denied as username or password is incorrect.

# Single combination

# In[24]:


import webbrowser

#Read username and password from files
username = open('username_file.txt').read()
password = open('userpassword_file.txt').read()

#Ask for username and password
input_username = input("Enter username: ")
input_password = input("Enter password: ")

#Check if they are correct
if input_username == username and input_password == password:
    print("Login successful, Opening Google Chrome...")
    webbrowser.open('https://www.google.com')
else:
    print("Permission denied. Incorrect username or password.")


# 

# Multiple combination

# In[28]:


import webbrowser

#Read usernames and passwords from files into lists
usernames = open('username_file_1.txt').read().splitlines()
passwords = open('userpassword_file_1.txt').read().splitlines()

#Ask for username and password input
input_username = input("Enter username: ")
input_password = input("Enter password: ")

#Check if the username and password match any valid pair
if input_username in usernames:
    # Get the index of the entered username
    index = usernames.index(input_username)

    # Check if the password at the same index matches the entered password
    if passwords[index] == input_password:
        print("Login successful, Opening Google Chrome...")
        webbrowser.open('https://www.google.com')
    else:
        print("Permission denied. Incorrect password.")
else:
    print("Permission denied. Username not found.")


# In[ ]:




