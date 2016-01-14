__author__ = 'jslvtr'


class StoreException(Exception):
    def __init__(self, message):
        self.message = message


class StoreNotFoundException(StoreException):
    pass