#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "7963861799"))
API_HASH = environ.get("API_HASH", "f6bb25d60317d38d10868c64c361f8d5")
BOT_TOKEN = environ.get("BOT_TOKEN", "7963861799:AAHoWDP1N0_tJL6XqNXphJLhV4gre-ApN54")
OWNER = int(environ.get("OWNER", "8118667253"))
CREDIT = "🌸S͜͡u͜͡j͜͡a͜͡l🌸"
AUTH_USER = os.environ.get('AUTH_USERS', '8118667253').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
