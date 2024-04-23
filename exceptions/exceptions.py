class BaseException(Exception):
    """Base class for exceptions"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


class FileNotFound(BaseException):
    """Raised when the specified cannot be found."""
    pass


class DataProcessingException(BaseException):
    """Exception related to data processing."""
    pass


class InvalidLineFormat(BaseException):
    """Raised when a line from the data has an incorrect format."""
    pass


class DuplicateRecordIdentifier(BaseException):
    """Raised when a duplicate record identifier is found."""
    pass

