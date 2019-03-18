from datetime import datetime
from decimal import Decimal
from re import RegexFlag
from typing import Any, Dict, List, Optional, Union, Pattern, Collection
from uuid import UUID

from django.core.files.base import File
from django.core.exceptions import ValidationError as ValidationError

EMPTY_VALUES: Any

_Regex = Union[str, Pattern[str]]

def _lazy_re_compile(regex: _Regex, flags: int = ...): ...

class RegexValidator:
    regex: _Regex = ...
    message: Any = ...
    code: str = ...
    inverse_match: bool = ...
    flags: int = ...
    def __init__(
        self,
        regex: Optional[_Regex] = ...,
        message: Optional[str] = ...,
        code: Optional[str] = ...,
        inverse_match: Optional[bool] = ...,
        flags: Optional[RegexFlag] = ...,
    ) -> None: ...
    def __call__(self, value: Optional[str]) -> None: ...

class URLValidator(RegexValidator):
    ul: str = ...
    ipv4_re: str = ...
    ipv6_re: str = ...
    hostname_re: Any = ...
    domain_re: Any = ...
    tld_re: Any = ...
    host_re: Any = ...
    schemes: Any = ...
    def __init__(self, schemes: Optional[Collection[str]] = ..., **kwargs: Any) -> None: ...

integer_validator: Any

def validate_integer(value: Optional[Union[float, str]]) -> None: ...

class EmailValidator:
    message: Any = ...
    code: str = ...
    user_regex: Any = ...
    domain_regex: Any = ...
    literal_regex: Any = ...
    domain_whitelist: Any = ...
    def __init__(
        self, message: Optional[str] = ..., code: Optional[str] = ..., whitelist: Optional[Collection[str]] = ...
    ) -> None: ...
    def __call__(self, value: Optional[str]) -> None: ...
    def validate_domain_part(self, domain_part: str) -> bool: ...

validate_email: Any
slug_re: Any
validate_slug: Any
slug_unicode_re: Any
validate_unicode_slug: Any

def validate_ipv4_address(value: str) -> None: ...
def validate_ipv6_address(value: str) -> None: ...
def validate_ipv46_address(value: str) -> None: ...

ip_address_validator_map: Any

def ip_address_validators(protocol: str, unpack_ipv4: bool) -> Any: ...
def int_list_validator(
    sep: str = ..., message: None = ..., code: str = ..., allow_negative: bool = ...
) -> RegexValidator: ...

validate_comma_separated_integer_list: Any

class BaseValidator:
    message: Any = ...
    code: str = ...
    limit_value: Any = ...
    def __init__(self, limit_value: Any, message: Optional[str] = ...) -> None: ...
    def __call__(self, value: Any) -> None: ...
    def compare(self, a: bool, b: bool) -> bool: ...
    def clean(self, x: Any) -> Any: ...

class MaxValueValidator(BaseValidator):
    message: Any = ...
    code: str = ...
    def compare(self, a: Union[datetime, Decimal, float], b: Union[datetime, Decimal, float]) -> bool: ...

class MinValueValidator(BaseValidator):
    message: Any = ...
    code: str = ...
    def compare(self, a: Union[datetime, Decimal, float], b: Union[datetime, Decimal, float]) -> bool: ...

class MinLengthValidator(BaseValidator):
    message: Any = ...
    code: str = ...
    def compare(self, a: int, b: int) -> bool: ...
    def clean(self, x: str) -> int: ...

class MaxLengthValidator(BaseValidator):
    message: Any = ...
    code: str = ...
    def compare(self, a: int, b: int) -> bool: ...
    def clean(self, x: Union[bytes, str]) -> int: ...

class DecimalValidator:
    messages: Any = ...
    max_digits: int = ...
    decimal_places: int = ...
    def __init__(self, max_digits: Optional[Union[int, str]], decimal_places: Optional[Union[int, str]]) -> None: ...
    def __call__(self, value: Decimal) -> None: ...

class FileExtensionValidator:
    message: Any = ...
    code: str = ...
    allowed_extensions: List[str] = ...
    def __init__(
        self,
        allowed_extensions: Optional[Collection[str]] = ...,
        message: Optional[str] = ...,
        code: Optional[str] = ...,
    ) -> None: ...
    def __call__(self, value: File) -> None: ...

def get_available_image_extensions() -> List[str]: ...
def validate_image_file_extension(value: File) -> None: ...

class ProhibitNullCharactersValidator:
    message: Any = ...
    code: str = ...
    def __init__(self, message: Optional[str] = ..., code: Optional[str] = ...) -> None: ...
    def __call__(self, value: Optional[Union[Dict[Any, Any], str, UUID]]) -> None: ...
