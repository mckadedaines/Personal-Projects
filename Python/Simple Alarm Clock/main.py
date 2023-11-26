# Create an alarm clock where the user can set a specific time, and when that time is reached, 
# the program should make a sound or display a message.
# Steps:
# - Takes the users input for when the alarm clock should go off (DONE)
# - When it hits the users time, alert the user with a message or sound

from datetime import datetime
import time

def main():
    usersTime = input("When should the alarm clock go off (HH:MM AM/PM)?: ")

    try:
        alarm_time = datetime.strptime(usersTime, "%I:%M %p")

        while True:
            time.sleep(1)
            now = datetime.now()
            
            if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
                print("ALARM!!!")
                break
    except ValueError:
        print("Invalid Input. Please enter a time in this format - HH:MM AM/PM.")

main()