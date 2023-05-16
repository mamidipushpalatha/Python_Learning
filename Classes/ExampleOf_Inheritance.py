'''streaming data app- stream,filestream,networkstream. 
check if streaming data is opened or closed or reponed or reclosed'''

from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = True

    @abstractmethod
    def read(self):
        pass

    def open(self):
        if self.opened:
            self.opened = True
            raise InvalidOperationError("Stream is already opened")
        print("opened streaming")

    def close(self):
        if self.opened:
            self.opened = True
            raise InvalidOperationError("Stream is already closed")
        print("closed streaming")


class FileStream(Stream):
    def read(self):
        print("reading data from file")


class networkStream(Stream):
    def read(self):
        print("reading data from file network ")


class MemoryStream(Stream):
    def read(self):
        print("reading data from file memory ")


stream = networkStream()
stream.read()
# stream.open()
stream.close()
