# . Write a function to split a given string on hyphens (-) and display each substring on a new line.
# You must:
# - Solve it using an inbuilt function (split()).
# - Solve it without using any inbuilt split functions — by using loops and conditions.
# Given:
# sentence = "Emma-is-a-data-scientist"
# Expected Output:
# Emma
# is
# a
# data
# scientist
# def split_inbuilt(sent):
#     substring=sent.split('-')
#     for sub in substring:
#         print(sub)
# split_inbuilt("Emma-is-a-date-scientist")        

# def split_no(sent):
#     substring=""
#     for i in sent:
#         if i!="-":
#             substring=substring+i
#         else:
#             print(substring)
#             substring=""
#     print(substring)        
# split_no("Emma-is-a-data-scientist")            
            


# 2. Write a Python program to reverse a given string in two ways:
# - Using an inbuilt function or slicing
# - Without using any inbuilt functions/Slicing
# Given:
# str1 = "Python"
# Expected Output:
# nohtyP

# def reverse_inbuilt(a):
#     print(a[::-1])
# reverse_inbuilt("Python")    

# def reverse_no(a):
#     rev=""
#     for i in a:
#         rev=i+rev
#     print(rev)

# reverse_no("Python")

# 3. Write a Python program to count the number of consonants in a given string.
# Input:
# Hello World
# Output:
# Number of consonants: 7
# def count_const(a):
#     count=0
#     vowels="aeiouAEIOU"
#     for i in a:
#         if i in vowels or i==" ":
#             continue
#         else:
#             count=count+1
#             print(count)
# count_const("Hello World")                

# 4.  Write a Python program to remove all spaces from a given string.
# Input:
# Python is awesome
# Output:
# Pythonisawesome
# def remove_space(a):
#     result=""
#     for i in a:
#         if i!=" ":
#             result=result+i
#     print(result)
# remove_space("Python is awesome")  


# Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:
# It has at least 8 characters and  atleast one special character (!@#$%^&*).
# Print whether the password is strong or not.
# Input:
# Password: my@password
# Output:
# Password is strong
# Input:
# Password: python123
# Output:
# Password is not strong
# def password(pwd):
#     spe_char="!@#$%^&*"
#     if len (pwd)>=8:
#         for i in pwd:
#             if i in spe_char:
#                 return "Password is strong"
#         return "Password is not strong"    
               
        
# print(password("python123"))                