# Modify Problem01 and print a specific message that is related to the number of cookies.
#• If the cookie number is between 1 and 10 (less than 10), print “Are you sure it’s enough?”
#• If the cookie number is between 10 and 20 (less than 20), print “I agree, cookies are delicious!”
#• If the cookie number is between 20 and 50 (less than 51), print “Be careful, it’s getting too much!”
#• If the cookie number is more than 50, print “No way, it’s getting too much!”, and modify the value to be 50.
#• For any other cases, print “Something must be wrong, I’ll give you 10 cookies.” and modify the value to be 10

# What's your name? Charlie
# How many cookies would you like to have? 3
# Hello, Charlie!
#Are you sure it's enough?
#Here are your cookies:
#Cookie
#Cookie
#Cookie

#What's your name? Rose
#How many cookies would you like to have? 12
#Hello, Rose!
#I agree, cookies are delicious!
#Here are your cookies:
#Cookie
#Cookie
#Cookie
#Cookie
#Cookie
#Cookie
#Cookie
#Cookie
#Cookie
#Cookie
#Cookie
#Cookie

print("Welcome to the cookie program!")
name, cookiecount = input("Enter your name and the number of cookies you need, seperated by a ',':").split(',')

print('Hello ', name, "!")

try:
    cookiecount = int(cookiecount)

    if ((cookiecount > 1) and (cookiecount < 10)):
        print("Are you sure it's enough?")
        print("Here are your cookies: \n", "Cookie \n" *int(cookiecount))
    elif ((cookiecount >= 10) and (cookiecount < 20)):
        print("I agree, cookies are delicious!")
        print("Here are your cookies: \n", "Cookie \n" *int(cookiecount))
    elif ((cookiecount >= 20) and (cookiecount <= 50)):
        print("Be careful, it's getting too much!")
        print("Here are your cookies: \n", "Cookie \n" *int(cookiecount))
    elif cookiecount > 50:
        print("No way, it's getting too much!")
        print("Here are your cookies: \n", "Cookie \n" *10)
except: 
    print("Something must be wrong, I'll give you 10 cookies")
    print("Here are your cookies: \n", "Cookie \n" *10)
    



