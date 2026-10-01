# ────═◈═─ HANDLES.PY - COMPATIBILITY FILE ─═◈═────
# This file is kept for backward compatibility.
# All handlers are now in bot.py

from bot import PikachuProtectionBot

# Re-export the bot class as Handlers for compatibility
Handlers = PikachuProtectionBot

# Also export db and utils if needed
from database import Database
from utils import Utils
from config import Config

db = Database()
utils = Utils()

# ────═◈═─ END OF FILE ─═◈═────
