import datetime as dt

class console:

    def log(text: str):
        content = _category.LOG + text
        print(f'[ {_date.now()} ] {content}', end='')

    def logl(text: str):
        content = _category.LOG + text
        print(f'[ {_date.now()} ] {content}')

    def info(text: str):
        content = _category.INFO + text
        print(f'[ {_date.now()} ] {content}')

    def debug(text: str):
        content = _category.DEBUG + text
        print(f'[ {_date.now()} ] {content}')

    def success(text: str):
        content = _category.SUCCESS + text
        print(f'[ {_date.now()} ] {content}')

    def warn(text: str):
        content = _category.WARN + text
        print(f'[ {_date.now()} ] {content}')

    def error(text: str):
        content = _category.ERROR + text
        print(f'[ {_date.now()} ] {content}')

class _colors:
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
    LOG = _colors.NORMAL + "LOG" + _colors.RESET + "     : "
    INFO = _colors.INFO + "INFO" + _colors.RESET + "    : "
    DEBUG = _colors.DEBUG + "DEBUG" + _colors.RESET + "   : "
    SUCCESS = _colors.SUCCESS + "SUCCESS" + _colors.RESET + " : "
    WARN = _colors.WARN + "WARN" + _colors.RESET + "    : "
    ERROR = _colors.ERROR + "ERROR" + _colors.RESET + "   : "

class _date:
    def now():
        return dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")