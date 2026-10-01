from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboards:
    
    @staticmethod
    def main_menu(is_premium=False):
        """Main menu keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("📊 sᴛᴀᴛs", callback_data="stats"),
                InlineKeyboardButton("⚙️ sᴇᴛᴛɪɴɢs", callback_data="settings")
            ],
            [
                InlineKeyboardButton("📖 ʜᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("ℹ️ ᴀʙᴏᴜᴛ", callback_data="about")
            ],
            [
                InlineKeyboardButton("👥 sᴛᴀғғ", callback_data="staff"),
                InlineKeyboardButton("🔄 SG", callback_data="sg")
            ],
            [
                InlineKeyboardButton("📜 ʜɪsᴛᴏʀʏ", callback_data="history"),
                InlineKeyboardButton("💬 ᴄʜᴀᴛ", callback_data="chat")
            ],
            [
                InlineKeyboardButton("👑 ʀᴏʟᴇs", callback_data="roles")
            ]
        ]
        
        if is_premium:
            keyboard.append([
                InlineKeyboardButton("💎 ᴘʀᴇᴍɪᴜᴍ", callback_data="premium")
            ])
        
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def settings_menu():
        """Settings menu keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("👋 ᴡᴇʟᴄᴏᴍᴇ", callback_data="toggle_welcome"),
                InlineKeyboardButton("👋 ɢᴏᴏᴅʙʏᴇ", callback_data="toggle_goodbye")
            ],
            [
                InlineKeyboardButton("🛡️ ᴀɴᴛɪ-sᴘᴀᴍ", callback_data="toggle_antispam"),
                InlineKeyboardButton("🔗 ᴀɴᴛɪ-ʟɪɴᴋ", callback_data="toggle_antilink")
            ],
            [
                InlineKeyboardButton("🔞 ᴀɴᴛɪ-18+", callback_data="toggle_anti18")
            ],
            [
                InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def toggle_keyboard(setting_name, current_value):
        """Toggle on/off keyboard for settings"""
        keyboard = [
            [
                InlineKeyboardButton(
                    f"{'✅' if current_value else '❌'} ᴛᴏɢɢʟᴇ",
                    callback_data=f"toggle_{setting_name}"
                )
            ],
            [
                InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="settings")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def premium_keyboard():
        """Premium features keyboard"""
        keyboard = [
            [
                InlineKeyboardButton("💰 ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ", callback_data="buy_premium"),
                InlineKeyboardButton("💎 ᴄʜᴇᴄᴋ sᴛᴀᴛᴜs", callback_data="check_premium")
            ],
            [
                InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="main_menu")
            ]
        ]
        return InlineKeyboardMarkup(keyboard)
    
    @staticmethod
    def role_keyboard():
        """Role selection keyboard"""
        keyboard = [
            [InlineKeyboardButton("👑 Fᴏᴜɴᴅᴇʀ", callback_data="role_founder")],
            [InlineKeyboardButton("⚜️ Cᴏ-Fᴏᴜɴᴅᴇʀ", callback_data="role_cofounder")],
            [InlineKeyboardButton("👔 Aᴅᴍɪɴ", callback_data="role_admin")],
            [InlineKeyboardButton("👷 Mᴏᴅᴇʀᴀᴛᴏʀ", callback_data="role_moderator")],
            [InlineKeyboardButton("🙊 Mᴜᴛᴇʀ", callback_data="role_muter")],
            [InlineKeyboardButton("🛃 Cʜᴀᴛ Cʟᴇᴀɴᴇʀ", callback_data="role_cleaner")],
            [InlineKeyboardButton("⛑ Hᴇʟᴘᴇʀ", callback_data="role_helper")],
            [InlineKeyboardButton("🔓 Fʀᴇᴇ", callback_data="role_free")],
            [InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="main_menu")]
        ]
        return InlineKeyboardMarkup(keyboard)
