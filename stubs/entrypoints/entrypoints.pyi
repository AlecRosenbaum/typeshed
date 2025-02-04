import sys
from _typeshed import Self
from collections.abc import Iterator, Sequence
from typing import Any

if sys.version_info >= (3, 0):
    from configparser import ConfigParser
else:
    from ConfigParser import ConfigParser

if sys.version_info >= (3, 8):
    from re import Pattern
else:
    from typing import Pattern

entry_point_pattern: Pattern[str]
file_in_zip_pattern: Pattern[str]

class BadEntryPoint(Exception):
    epstr: str
    def __init__(self, epstr: str) -> None: ...
    @staticmethod
    def err_to_warnings() -> Iterator[None]: ...

class NoSuchEntryPoint(Exception):
    group: str
    name: str
    def __init__(self, group: str, name: str) -> None: ...

class EntryPoint:
    name: str
    module_name: str
    object_name: str
    extras: Sequence[str] | None
    distro: Distribution | None
    def __init__(
        self, name: str, module_name: str, object_name: str, extras: Sequence[str] | None = ..., distro: Distribution | None = ...
    ) -> None: ...
    def load(self) -> Any: ...
    @classmethod
    def from_string(cls: type[Self], epstr: str, name: str, distro: Distribution | None = ...) -> Self: ...

class Distribution:
    name: str
    version: str
    def __init__(self, name: str, version: str) -> None: ...

def iter_files_distros(
    path: Sequence[str] | None = ..., repeated_distro: str = ...
) -> Iterator[tuple[ConfigParser, Distribution | None]]: ...
def get_single(group: str, name: str, path: Sequence[str] | None = ...) -> EntryPoint: ...
def get_group_named(group: str, path: Sequence[str] | None = ...) -> dict[str, EntryPoint]: ...
def get_group_all(group: str, path: Sequence[str] | None = ...) -> list[EntryPoint]: ...
