"""
Using conditional statements to allow the program to print out different
time of the day based on the current time.
"""

import datetime

# Get the current hour
current_hour = datetime.datetime.now().hour

# lets see what this 'hour' or current time is
print(current_hour)
# output: 4 (it;s 4:11am right now)

# Determine the time of day based on the current hour
if 5 <= current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 18:
    print("Good afternoon!")
elif 18 <= current_hour < 22:
    print("Good evening!")
else:
    print("Good night!")


# output:
# 4                         <- current hour
# Good night!               <- message based on current hour


# This does not bring about intelligence per say, but it seems like it if we code enough 'rules'.
