# exception/DuplicateEntryException.py
class DuplicateEntryException(Exception):
    def __init__(self, message="Duplicate entry found"):
        self.message = message
        super().__init__(self.message)
