# Write a script that asks the name of the user, and the number of cookies they want to have. Print out a welcome message with the name of the user and the cookies one by one. 
# Example output:
# What's your name? Charlie
# How many cookies would you like to have? 3
# Hello, Charlie!
# Here are your cookies:
# Cookie
# Cookie
# Cookie

print("Welcome to the cookie program!")
name, cookiecount = input("Enter your name and the number of cookies you need, seperated by a ',':").split(',')
print('Hello ', name, "!\n", "Here are your cookies:")
print("Cookie \n" *int(cookiecount))