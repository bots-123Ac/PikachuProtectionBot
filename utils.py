import re
import html
from datetime import datetime

class Utils:
    @staticmethod
    def format_user_mention(user):
        """Format user mention with stylish font"""
        if user.username:
            return f"@{user.username}"
        return f"<a href='tg://user?id={user.id}'>{html.escape(user.first_name)}</a>"
    
    @staticmethod
    def parse_duration(duration_str: str) -> int:
        """Parse duration string to seconds"""
        if not duration_str:
            return 300
        
        unit_map = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400,
            'w': 604800
        }
        
        match = re.match(r'(\d+)([smhdw])', duration_str.lower())
        if match:
            value, unit = match.groups()
            return int(value) * unit_map.get(unit, 1)
        return int(duration_str) if duration_str.isdigit() else 300
    
    @staticmethod
    def format_duration(seconds: int) -> str:
        """Format seconds to human readable duration"""
        if seconds < 60:
            return f"{seconds}s"
        elif seconds < 3600:
            minutes = seconds // 60
            return f"{minutes}m"
        elif seconds < 86400:
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            return f"{hours}h {minutes}m" if minutes else f"{hours}h"
        else:
            days = seconds // 86400
            hours = (seconds % 86400) // 3600
            return f"{days}d {hours}h" if hours else f"{days}d"
    
    @staticmethod
    def check_link(text: str) -> bool:
        """Check if text contains links"""
        url_pattern = re.compile(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+])|[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        )
        return bool(url_pattern.search(text))
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Clean and format text"""
        if not text:
            return ""
        text = html.escape(text)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
