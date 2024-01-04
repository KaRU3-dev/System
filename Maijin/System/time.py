"""
Get date and time
"""

import datetime as dt

def now():
    """
    Get current date and time in format: YYYY-MM-DD HH:MM:SS
    @type: private
    """
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
