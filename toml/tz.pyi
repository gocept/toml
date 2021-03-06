from datetime import tzinfo
from typing import Any

class TomlTz(tzinfo):
    def __init__(self, toml_offset: Any) -> None: ...
    def __deepcopy__(self, memo: Any): ...
    def tzname(self, dt: Any): ...
    def utcoffset(self, dt: Any): ...
    def dst(self, dt: Any): ...
