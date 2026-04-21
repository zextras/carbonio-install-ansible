from __future__ import annotations

from typing import Any


def _is_ascii_alnum_or_hyphen(value: str) -> bool:
    for char in value:
        if not (char.isascii() and (char.isalnum() or char == "-")):
            return False
    return True


def _is_ascii_alpha(value: str) -> bool:
    for char in value:
        if not (char.isascii() and char.isalpha()):
            return False
    return True


def fqdn_strict(value: Any) -> bool:
    if not isinstance(value, str):
        return False

    if not value:
        return False

    if value != value.strip():
        return False

    if len(value) > 253:
        return False

    if "." not in value:
        return False

    labels = value.split(".")

    if len(labels) < 2:
        return False

    for label in labels:
        if not label:
            return False

        if len(label) > 63:
            return False

        if label[0] == "-" or label[-1] == "-":
            return False

        if not _is_ascii_alnum_or_hyphen(label):
            return False

    tld = labels[-1]

    if len(tld) < 2:
        return False

    if not _is_ascii_alpha(tld):
        return False

    return True


class TestModule:
    def tests(self) -> dict[str, Any]:
        return {
            "fqdn_check": fqdn_check,
        }