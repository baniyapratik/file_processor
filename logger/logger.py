import inspect
from datetime import datetime


class LogFactory(object):
    def __init__(self, name=None):
        self.name = name
        if name is None:
            try:
                frm = inspect.stack()[1]
                mod = inspect.getmodule(frm[0])
                self.name = mod.__name__
            except Exception as err:
                print(f"Exception occured. {err}")

    TimeFormat = "%Y-%m-%d-T%H-%M-%S"

    @staticmethod
    def yellow(msg):
        return f"\033[93m{msg}\033[0m"

    @staticmethod
    def red(msg):
        return f"\033[91m{msg}\033[0m"

    @staticmethod
    def green(msg):
        return f"\033[32m{msg}\033[0m"

    @staticmethod
    def bold(msg):
        return f"\033[1m{msg}\033[0m"

    @staticmethod
    def __stamp__(tag, name, msg):
        timestamp = datetime.now().strftime(LogFactory.TimeFormat)
        return f"{tag}{timestamp}[{name}]>{msg}"

    def info(self, msg):
        """Print info on stdout"""
        prefix = '-Info----'
        print(self.__stamp__(prefix, self.name, msg))

    def warning(self, msg):
        """Print warning on stdout"""
        prefix = '-Warning-'
        print(LogFactory.yellow(self.__stamp__(prefix, self.name, msg)))

    def error(self, msg):
        """Print error on stdout"""
        prefix = '-Error---'
        print(LogFactory.red(self.__stamp__(prefix, self.name, msg)))

    def debug(self, msg):
        """Print debug on stdout"""
        prefix = '-Debug---'
        print(LogFactory.bold(self.__stamp__(prefix, self.name, msg)))

    def success(self, msg):
        """Print success on stdout"""
        prefix = '-Success-'
        print(LogFactory.green(self.__stamp__(prefix, self.name, msg)))