# Write a script that calculates the average of some integers. 
# First ask how many numbers the user has, then calculate the average and print it. 
# Example output:
# How many numbers do you have? 3
# Give me one of them: 6
# Give me one of them: 6
# Give me one of them: 3
# Your average is 5

import numpy as np

print("Welcome to the averaging program!")
try:
    numcount = int(input("How many numbers do you have?: "))

    numlist = []
    while (numcount > 0):
        numlist.append(int(input("Give me one of them: ")))
        numcount = numcount -1 

    print("Your average is: ", int(np.average(numlist)))
except:
    print("Either the count or the numbers are not valid, existing...")

