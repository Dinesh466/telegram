import asyncio
from telethon import TelegramClient, events
from telegram import Bot
import logging

# Replace these with your own values
api_id = '23310585'  
api_hash = '4f1c9cafb74c4fac84b9656cdc624bbc' 
channel_username = "new_sol_coins"  
bot_token = "7792444669:AAFkpBoV7rccj2yGwJQhjcL0VqFeG4qHE5U"  
bot_chat_id = "7908886159"  


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Initialize the Telegram client (for monitoring the channel)
client = TelegramClient('session_name', api_id, api_hash)

# Initialize the bot (for sending messages)
bot = Bot(token=bot_token)

# Event handler for new messages in the channel
@client.on(events.NewMessage(chats=channel_username))
async def handle_channel_message(event):
    text = event.message.message
    logger.info(f"New message in channel: {text}")

    try:
        # Forward the message to the bot
        await bot.send_message(chat_id=bot_chat_id, text=text)
        logger.info("Message forwarded to the bot.")
    except Exception as e:
        logger.error(f"Failed to forward message to bot: {e}")

# Function to start monitoring the channel
async def start_monitoring():
    while True:
        try:
            logger.info("Starting channel monitoring...")
            await client.start()
            await client.run_until_disconnected()
        except Exception as e:
            logger.error(f"Error in monitoring: {e}. Restarting in 10 seconds...")
            await asyncio.sleep(10)  # Wait before restarting

# Main function
async def main():
    await start_monitoring()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Script stopped by user.")