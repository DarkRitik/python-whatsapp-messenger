"""
twilio
datetime module
time
"""
"""
1 - twilio client setup
2 - user inputs
3 - scheduling logic
4 - send message
"""
# Step-1 install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Step-2 twilio credentials
account_sid = '' # Put your SID
auth_token = ''  # Put your Token

client = Client(account_sid, auth_token)

# Step-3 desgine send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='', # Put Your Number where you getting it from twilio
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occurred')

# Step-4 user input
name = input('Enter the recipinet name: ')
recipient_number = input('Enter the recipient Whatsapp number with country code: ')
message_body = input(f'enter the message you want to send to {name}: ')

# Step-5 parse date/time and calculate dela
date_str = input('enter the date to send the message (YYYY-MM-DD): ')
time_str = input('enter the time to send the message (HH:MM in 24 Hour format): ')

# datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_secounds = time_difference.total_seconds()

if delay_secounds <=0:
    print('The specified time is in the past. Please enter a future date and time')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

# wait until the scheduled time 
time.sleep(delay_secounds) #1000

# Send the message
send_whatsapp_message(recipient_number, message_body)