import os

class Config:
    # Bot Configuration
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_NAME = os.environ.get("BOT_NAME", "── ᴘɪᴋᴀᴄʜᴜ ✗ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ ──")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Pikachu_Protection_Robot")
    
    # Owner Configuration
    OWNER_ID = int(os.environ.get("OWNER_ID", "7790607144"))
    OWNER_NAME = os.environ.get("OWNER_NAME", "⏤͟͞ 𝐂𝐑𝐀𝐙𝐘 𝐁𝐎𝐘 ᭄࿐")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "@CrazyyCore")
    
    # Premium Users (Comma separated)
    PREMIUM_USERS = [int(id.strip()) for id in os.environ.get("PREMIUM_USERS", "7790607144").split(",") if id.strip()]
    
    # Moderation Settings
    MAX_WARNINGS = int(os.environ.get("MAX_WARNINGS", "3"))
    MUTE_DURATION = int(os.environ.get("MUTE_DURATION", "300"))
    FLOOD_LIMIT = int(os.environ.get("FLOOD_LIMIT", "5"))
    
    # Log Channel
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003424504397"))
    
    # Database
    MONGO_URI = os.environ.get("MONGO_URI", "")
    DB_NAME = os.environ.get("DB_NAME", "pikachu_protection")
    
    # Port for Flask
    PORT = int(os.environ.get("PORT", 8080))
