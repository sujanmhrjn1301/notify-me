import discord
import os
from dotenv import load_dotenv
from app.discord_bot.sms import send_sms  # Ensure the path is correct

# Load environment variables from .env file
load_dotenv()

# Discord bot token
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Initialize Discord client
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.presences = True 
bot = discord.Client(intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the server"))
    print(f"{bot.user} is now ready to respond!")

# Event: When a message is sent in the server
@bot.event
async def on_message(message):
    your_user_id = int(os.getenv('YOUR_DISCORD_USER_ID'))  # Get your Discord user ID

    # Check if the message is 'hello' and respond
    if message.content.lower() == 'hello':
        await message.channel.send(f'Hello {message.author.name}! The bot is working.')

    # Check if you're mentioned in the message
    if bot.user in message.mentions or your_user_id in [mention.id for mention in message.mentions] or message.mention_everyone:
        member = message.guild.get_member(your_user_id)

        # Check if the member is found
        if member is not None:
            # Check and log the member's current status
            current_status = member.status
            print(f"{member.name}'s current status: {current_status}")

            # Send SMS only if the member is offline
            if current_status == discord.Status.offline:
                # Include server name, channel name, and message content
                message_content = (
                    f"SERVER: **{message.guild.name}** | "
                    f"USER: **{message.author.name}** | "
                    f"CHANNEL: **{message.channel.name}** | "
                    f"MESSAGE: {message.content.replace(str(your_user_id), 'mr.eiji')}"
                )
                await message.channel.send(f'MR.EIJI is currently offline. Notifying via SMS...')
                # Send SMS to your phone using Twilio
                send_sms(message_content)
                print('You were mentioned while offline, SMS sent.')
            else:
                print(f'{member.name} is online, no SMS sent.')
        else:
            print('Member not found.')
