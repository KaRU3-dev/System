"""
Console output with color and date.\n
This class is joined with module Maijin.System.\n
@type: public
@usedClass: color, _category, _date
@example:
>>> System.console.log('Hello World!')     # With no new line
>>> System.console.logl('Hello World!')    # With new line
>>> System.console.info('Hello World!')    # Info
>>> System.console.debug('Hello World!')   # Debug
>>> System.console.success('Hello World!') # Success
>>> System.console.warn('Hello World!')    # Warn
>>> System.console.error('Hello World!')   # Error
"""

import Maijin.System.time as t
import Maijin.System.colors as color

def log(text: str=""):
    """
    White text with no new line
    @output: [ YYYY-MM-DD HH:MM:SS ] LOG     : Hello World!
    @setColor: LOG = White
    >>> System.console.log('Hello World!')
    """
    content = _category.LOG + text
    print(f'[ {t.now()} ] {content}', end='')

def logl(text: str=""):
    """
    White text with new line
    @output: [ YYYY-MM-DD HH:MM:SS ] LOG     : Hello World!(\\n)
    @setColor: LOG = White
    >>> System.console.logl('Hello World!')
    """
    content = _category.LOG + text
    print(f'[ {t.now()} ] {content}')

def info(text: str=""):
    """
    Cyan text with new line
    @output: [ YYYY-MM-DD HH:MM:SS ] INFO    : Hello World!(\\n)
    @setColor: INFO = Cyan
    >>> System.console.info('Hello World!')
    """
    content = _category.INFO + text
    print(f'[ {t.now()} ] {content}')

def debug(text: str=""):
    """
    Blue text with new line
    @output: [ YYYY-MM-DD HH:MM:SS ] DEBUG   : Hello World!(\\n)
    @setColor: DEBUG = Blue
    >>> System.console.debug('Hello World!')
    """
    content = _category.DEBUG + text
    print(f'[ {t.now()} ] {content}')

def success(text: str=""):
    """
    Green text with new line
    @output: [ YYYY-MM-DD HH:MM:SS ] SUCCESS : Hello World!(\\n)
    @setColor: SUCCESS = Green
    >>> System.console.success('Hello World!')
    """
    content = _category.SUCCESS + text
    print(f'[ {t.now()} ] {content}')

def warn(text: str=""):
    """
    Yellow text with new line
    @output: [ YYYY-MM-DD HH:MM:SS ] WARN    : Hello World!(\\n)
    @setColor: WARN = Yellow
    >>> System.console.warn('Hello World!')
    """
    content = _category.WARN + text
    print(f'[ {t.now()} ] {content}')

def error(text: str=""):
    """
    Red text with new line
    @output: [ YYYY-MM-DD HH:MM:SS ] ERROR   : Hello World!(\\n)
    @setColor: ERROR = Red
    >>> System.console.error('Hello World!')
    """
    content = _category.ERROR + text
    print(f'[ {t.now()} ] {content}')

class _category:
    """
    Log category
    @type: private
    """
    LOG = color.NORMAL + "LOG" + color.RESET + "     : "
    INFO = color.INFO + "INFO" + color.RESET + "    : "
    DEBUG = color.DEBUG + "DEBUG" + color.RESET + "   : "
    SUCCESS = color.SUCCESS + "SUCCESS" + color.RESET + " : "
    WARN = color.WARN + "WARN" + color.RESET + "    : "
    ERROR = color.ERROR + "ERROR" + color.RESET + "   : "
