import os
import requests
import pymongo
from pyrogram import Client, filters

# Initialize bot (replace with your own values)
API_ID = "29478593"  # Your API ID
API_HASH = "24c3a9ded4ac74bab73cbe6dafbc8b3e"
BOT_TOKEN = "5527818445:AAE7TLprBfyUuQvYZsaOesQ0F-9C2sl2I80"
WEB_APP_URL = "https://corpse-x.github.io/XPROJECT"  # Your web app API endpoint

app = Client("xghost", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# MongoDB setup
mongo_client = pymongo.MongoClient("mongodb://localhost:3000/")
db = mongo_client["user_db"]
users_collection = db["users"]

# Command: /start
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Welcome to the bot! Use /signup or /login to get started.")

# Command: /signup
@app.on_message(filters.command("signup"))
async def signup(client, message):
    await message.reply("Please enter your email and password separated by a space, e.g., `email@example.com password`")

    @app.on_message(filters.text & ~filters.command)
    async def get_signup_info(client, message):
        try:
            email, password = message.text.split()
            # Call the web app API to register the user
            response = requests.post(f"{WEB_APP_URL}/signup", json={"email": email, "password": password})
            if response.status_code == 200:
                # Store user in MongoDB
                users_collection.insert_one({"user_id": message.from_user.id, "email": email})
                await message.reply("Signup successful! You can now /login.")
            else:
                await message.reply("Signup failed. Try again.")
        except ValueError:
            await message.reply("Please provide valid email and password.")

# Command: /login
@app.on_message(filters.command("login"))
async def login(client, message):
    await message.reply("Please enter your email and password separated by a space, e.g., `email@example.com password`")

    @app.on_message(filters.text & ~filters.command)
    async def get_login_info(client, message):
        try:
            email, password = message.text.split()
            # Call the web app API to log in the user
            response = requests.post(f"{WEB_APP_URL}/login", json={"email": email, "password": password})
            if response.status_code == 200:
                await message.reply("Login successful! Welcome to the dashboard.")
            else:
                await message.reply("Login failed. Check your credentials.")
        except ValueError:
            await message.reply("Please provide valid email and password.")

# Command: /dashboard
@app.on_message(filters.command("dashboard"))
async def dashboard(client, message):
    user = users_collection.find_one({"user_id": message.from_user.id})
    if user:
        await message.reply(f"Welcome to your dashboard, {user['email']}!")
    else:
        await message.reply("Please log in using /login first.")

if __name__ == "__main__":
    app.run()