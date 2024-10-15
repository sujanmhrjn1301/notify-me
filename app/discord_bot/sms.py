import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_MESSAGING_SERVICE_SID = os.getenv('TWILIO_MESSAGING_SERVICE_SID')
USER_PHONE_NUMBER = os.getenv('USER_PHONE_NUMBER')

# Function to send SMS via Twilio
def send_sms(message_content):
    message_content = f"{message_content}"  # Adding context
    url = f'https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Messages.json'
    data = {
        'MessagingServiceSid': TWILIO_MESSAGING_SERVICE_SID,
        'Body': message_content,
        'To': USER_PHONE_NUMBER
    }
    try:
        response = requests.post(url, data=data, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
        if response.status_code == 201:
            print(f"SMS sent: {response.json()['sid']}")
        else:
            print(f"Failed to send SMS: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error: {str(e)}")
