import sys
from typing import Any

if sys.version_info < (3, 8):
    from typing_extensions import Protocol
else:
    from typing import Protocol

# Used internally by mypy_django_plugin.
class AnyAttrAllowed(Protocol):
    def __getattr__(self, item: str) -> Any:
        ...

    def __setattr__(self, item: str, value: Any) -> None:
        ...
