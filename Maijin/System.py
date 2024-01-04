"""
Maijin.System\n
Useful system functions.\n
@type: module
@class: console, _colors, _category, _date
\n\n
@example:
>>> import Maijin.System as System
>>> System.console.log('Hello World!')
[ 2021-01-01 00:00:00 ] LOG     : Hello World!
"""


import datetime as dt

class console:
    """
    Console output with color and date.\n
    This class is joined with module Maijin.System.\n
    @type: public
    @usedClass: _colors, _category, _date
    @example:
    >>> System.console.log('Hello World!')     # With no new line
    >>> System.console.logl('Hello World!')    # With new line
    >>> System.console.info('Hello World!')    # Info
    >>> System.console.debug('Hello World!')   # Debug
    >>> System.console.success('Hello World!') # Success
    >>> System.console.warn('Hello World!')    # Warn
    >>> System.console.error('Hello World!')   # Error
    """

    def log(text: str=""):
        """
        White text with no new line
        @output: [ YYYY-MM-DD HH:MM:SS ] LOG     : Hello World!
        @setColor: LOG = White
        >>> System.console.log('Hello World!')
        """
        content = _category.LOG + text
        print(f'[ {_date.now()} ] {content}', end='')

    def logl(text: str=""):
        """
        White text with new line
        @output: [ YYYY-MM-DD HH:MM:SS ] LOG     : Hello World!(\\n)
        @setColor: LOG = White
        >>> System.console.logl('Hello World!')
        """
        content = _category.LOG + text
        print(f'[ {_date.now()} ] {content}')

    def info(text: str=""):
        """
        Cyan text with new line
        @output: [ YYYY-MM-DD HH:MM:SS ] INFO    : Hello World!(\\n)
        @setColor: INFO = Cyan
        >>> System.console.info('Hello World!')
        """
        content = _category.INFO + text
        print(f'[ {_date.now()} ] {content}')

    def debug(text: str=""):
        """
        Blue text with new line
        @output: [ YYYY-MM-DD HH:MM:SS ] DEBUG   : Hello World!(\\n)
        @setColor: DEBUG = Blue
        >>> System.console.debug('Hello World!')
        """
        content = _category.DEBUG + text
        print(f'[ {_date.now()} ] {content}')

    def success(text: str=""):
        """
        Green text with new line
        @output: [ YYYY-MM-DD HH:MM:SS ] SUCCESS : Hello World!(\\n)
        @setColor: SUCCESS = Green
        >>> System.console.success('Hello World!')
        """
        content = _category.SUCCESS + text
        print(f'[ {_date.now()} ] {content}')

    def warn(text: str=""):
        """
        Yellow text with new line
        @output: [ YYYY-MM-DD HH:MM:SS ] WARN    : Hello World!(\\n)
        @setColor: WARN = Yellow
        >>> System.console.warn('Hello World!')
        """
        content = _category.WARN + text
        print(f'[ {_date.now()} ] {content}')

    def error(text: str=""):
        """
        Red text with new line
        @output: [ YYYY-MM-DD HH:MM:SS ] ERROR   : Hello World!(\\n)
        @setColor: ERROR = Red
        >>> System.console.error('Hello World!')
        """
        content = _category.ERROR + text
        print(f'[ {_date.now()} ] {content}')

class _colors:
    """
    Log colors
    @type: private
    """
    RESET = "\033[0m"          # Reset
    NORMAL = "\033[0m"         # Normal = Rest
    BOLD = "\033[1m"           # Bold = **Bold**
    UNDERLINE = "\033[4m"      # Underline = __Underline__
    BLINK = "\033[5m"          # Blink = ~~Blink~~
    HIDDEN = "\033[8m"         # Hidden = ??Hidden??
    STRIKETHROUGH = "\033[9m"  # Strikethrough = --Strikethrough--
    INFO = "\033[1;36m"        # Cyan
    DEBUG = "\033[1;34m"       # Blue
    SUCCESS = "\033[1;32m"     # Green
    WARN = "\033[1;33m"        # Yellow
    ERROR = "\033[1;31m"       # Red

class _category:
    """
    Log category
    @type: private
    """
    LOG = _colors.NORMAL + "LOG" + _colors.RESET + "     : "
    INFO = _colors.INFO + "INFO" + _colors.RESET + "    : "
    DEBUG = _colors.DEBUG + "DEBUG" + _colors.RESET + "   : "
    SUCCESS = _colors.SUCCESS + "SUCCESS" + _colors.RESET + " : "
    WARN = _colors.WARN + "WARN" + _colors.RESET + "    : "
    ERROR = _colors.ERROR + "ERROR" + _colors.RESET + "   : "

class _date:
    def now():
        """
        Get current date and time in format: YYYY-MM-DD HH:MM:SS
        @type: private
        """
        return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")