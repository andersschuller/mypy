# Stubs for threading

# NOTE: These are incomplete!

from typing import Any, Dict, Optional, Callable, TypeVar, Union

class Thread:
    name = ''
    ident = 0
    daemon = False

    def __init__(self, group: Any = None, target: Any = None, args: Any = (),
                 kwargs: Dict[Any, Any] = None,
                 verbose: Any = None) -> None: ...
    def start(self) -> None: ...
    def run(self) -> None: ...
    def join(self, timeout: float = 0.0) -> None: ...
    def is_alive(self) -> bool: ...

    # Legacy methods
    def getName(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def isDaemon(self) -> bool: ...
    def setDaemon(self, daemon: bool) -> None: ...

class Event:
    def is_set(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    # TODO can it return None?
    def wait(self, timeout: float = 0.0) -> bool: ...

class Lock:
    def acquire(self, blocking: bool = True, timeout: float = -1.0) -> bool: ...
    def release(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *args): ...

class RLock:
    def acquire(self, blocking: bool = True,
                timeout: float = -1.0) -> Optional[bool]: ...
    def release(self) -> None: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *args): ...

_T = TypeVar('_T')

class Condition:
    def acquire(self, blocking: bool = True, timeout: float = -1.0) -> bool: ...
    def release(self) -> None: ...
    def notify(self, n: int = 1) -> None: ...
    def notify_all(self) -> None: ...
    def wait(self, timeout: float = None) -> bool: ...
    def wait_for(self, predicate: Callable[[], _T], timeout: float = None) -> Union[_T, bool]: ...
    def __enter__(self) -> bool: ...
    def __exit__(self, *args): ...
