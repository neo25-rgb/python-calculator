from pathlib import Path

"""Utilities: Calculator and History implementations.

Completed implementations for Calculator and History according to the tests.
"""
from typing import List

class Calculator():
    """
    Rounding behavior:
    - If rounding_digits == 0, integer-like results should be returned as int.
    - Otherwise return a float rounded to rounding_digits.
    """
    rounding_digits = 0

    def __init__(self, round_digits: int = 0):
        self.rounding_digits = int(round_digits)

    def _round(self, value):
        if self.rounding_digits == 0:
            v = round(value, 0)
            try:
                if float(v).is_integer():
                    return int(v)
            except Exception:
                pass
            return int(v)
        else:
            return round(value, self.rounding_digits)

    
    def addtion(self, a, b):
        return self._round(a + b)

    def subtraction(self, a, b):
        return self._round(a - b)

    def multiplication(self, a, b):
        return self._round(a * b)

    def division(self, a, b):
        return self._round(a / b)

    def set_ound_digits(self, digits):
        self.rounding_digits = int(digits)


class History():
    """Simple history backed by a text file.

    - save(expression: str): appends the expression (with newline) to file.
    - restore() -> list[str]: returns list of lines (as strings). If file doesn't exist or is empty, return [].
    - clear(): empties the file.
    """
    filepath_ = ""
    def __init__(self, filepath: str):
        self.filepath_ = filepath

    def save(self, expression: str):
        Path(self.filepath_).parent.mkdir(parents=True, exist_ok=True)
        with open(self.filepath_, "a", encoding="utf-8") as f:
            f.write(expression.rstrip() + "\n")

    def restore(self) -> List[str]:
        if not Path(self.filepath_).exists():
            return []
        with open(self.filepath_, "r", encoding="utf-8") as f:
            lines = [line.rstrip("\n") for line in f.readlines() if line.strip() != ""]
        return lines

    def clear(self):
        open(self.filepath_, "w", encoding="utf-8").close()
