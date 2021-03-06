# Stubs for email.feedparser (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class BufferedSubFile:
    def __init__(self): ...
    def push_eof_matcher(self, pred): ...
    def pop_eof_matcher(self): ...
    def close(self): ...
    def readline(self): ...
    def unreadline(self, line): ...
    def push(self, data): ...
    def pushlines(self, lines): ...
    def __iter__(self): ...
    def __next__(self): ...

class FeedParser:
    policy = ...  # type: Any
    def __init__(self, _factory=None, *, policy=...): ...
    def feed(self, data): ...
    def close(self): ...

class BytesFeedParser(FeedParser):
    def feed(self, data): ...
