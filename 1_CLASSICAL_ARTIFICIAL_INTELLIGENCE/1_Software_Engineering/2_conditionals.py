"""
Using conditional statements to allow the program to print out different
time of the day based on the current time.
"""

import datetime

# Get the current hour
current_hour = datetime.datetime.now().hour

# lets see what this 'hour' or current time is
print(current_hour)
# output: 4 (it;s 4:11 am right now)

# Determine the time of day based on the current hour
if 5 <= current_hour < 12:                  # time from 5am to before 12pm noon.
    print("Good morning!")
# time from 12pm noon to before 6pm evening.
elif 12 <= current_hour < 18:
    print("Good afternoon!")
# time from 6pm evening to before 10pm night.
elif 18 <= current_hour < 22:
    print("Good evening!")
else:                                       # time from 10pm night to before 5am morning.
    print("Good night!")


# output:
# 4                                         <- current hour
# Good night!                               <- message based on current hour
