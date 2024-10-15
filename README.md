# Discord SMS Notification Bot
## Project Overview
### This project implements a Discord bot that sends SMS notifications when you are mentioned in a server while offline. Leveraging the Discord API and Twilio's SMS service, this bot enhances communication by ensuring that important messages reach you even when you're not actively online.

## Project Demo
![demo](https://github.com/user-attachments/assets/77dd60af-9bca-4fca-8e69-b1369b94fd6e)

## Features
### Mention Detection: 
The bot listens for messages in Discord servers and checks if you are mentioned or if the @everyone tag is used.
### SMS Notifications: 
If you are offline, the bot sends an SMS notification to your specified phone number, providing context about the message, including the server name, user, channel, and content.
### Discord Presence Management: 
The bot updates its status to indicate its readiness and monitor your presence in the server.
### User-Friendly Responses: 
The bot can respond to simple greetings and confirm its operational status.
Technologies Used
### Discord.py: 
A Python wrapper for the Discord API, facilitating easy interaction with Discord's features.
### Twilio: 
A cloud communications platform that allows sending SMS messages programmatically.
### Python: 
The primary programming language used for developing the bot.
### dotenv: 
A Python library to load environment variables from a .env file, ensuring sensitive data like tokens are not hard-coded.
## Getting Started
### Prerequisites
Python 3.7 or higher
A Discord bot token (create a bot on the Discord Developer Portal)
Twilio account credentials (Account SID, Auth Token, Messaging Service SID)
Your Discord User ID (to receive mentions)
### Installation
### Clone the repository: git clone https://github.com/sujanmhrjn1301/notify-me.git
cd notify-me
### Install the required packages:
pip install -r requirements.txt
### Set up your .env file with the necessary credentials:
#### DISCORD_BOT_TOKEN=your_discord_bot_token
#### TWILIO_ACCOUNT_SID=your_twilio_account_sid
#### TWILIO_AUTH_TOKEN=your_twilio_auth_token
#### TWILIO_MESSAGING_SERVICE_SID=your_twilio_messaging_service_sid
#### USER_PHONE_NUMBER=your_phone_number
#### YOUR_DISCORD_USER_ID=your_discord_user_id
### Running the Bot
To run the bot, execute:
python main.py
