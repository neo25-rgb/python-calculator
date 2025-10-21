# 🧮 Python Calculator

A simple calculator program that performs arithmetic operations on two numbers, supports result rounding, and maintains a history of calculations using file storage.

---

## 📘 Features

### Calculator
- Performs basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Supports **custom rounding precision** (e.g., 10 / 3 → 3.33 when rounding to 2 digits)
- Allows updating rounding digits at runtime

### History
- Saves expressions and results to a text file
- Restores previously saved expressions
- Clears all saved history

---

## 🧩 Class Overview

### `Calculator`
| Method | Description |
|---------|--------------|
| `__init__(round_digits)` | Initializes calculator with a rounding precision |
| `addition(a, b)` | Returns the sum of `a` and `b` |
| `subtraction(a, b)` | Returns the difference of `a` and `b` |
| `multiplication(a, b)` | Returns the product of `a` and `b` |
| `division(a, b)` | Returns the quotient of `a` and `b` |
| `set_round_digits(digits)` | Updates the rounding precision |
| `round_digits` *(property)* | Returns the current rounding digits |

### `History`
| Method | Description |
|---------|--------------|
| `save(expression: str)` | Saves a string expression to a file |
| `restore() -> list[str]` | Returns a list of saved expressions |
| `clear()` | Clears the history file |

---

## 🧪 Tests

Unit tests validate:
- Correct arithmetic results and rounding
- Division by zero handling
- File-based history operations (save, restore, clear)

To run the tests:
```bash
python -m unittest test_calculator.py
```



You must include spaces between the numbers and operator.  
Invalid expressions are rejected with an explanatory message.

---

## 💻 The `app.py` Program

`app.py` is the **main application script** that brings everything together.  
It acts as the **user interface** for your calculator system.

### Here's what it does step-by-step:
1. **Displays a colorful welcome screen** with usage instructions.
2. **Creates**:
   - A `Calculator` object (from `utils.py`) to perform operations.
   - A `History` object to manage a text file (`History.txt`).
3. **Listens for user input** in an infinite loop:
   - `h` → Displays the last 5 saved expressions (most recent first)
   - `c` → Clears the history file
   - `r` → Lets the user set how many decimal digits results are rounded to
   - `q` → Quits the program
   - Any valid arithmetic expression → Computes and prints the result, then saves it to history
4. **Validates input expressions** using the `is_valid_expression()` helper.
5. **Prints results neatly** and appends them to the history file.

---

### Example Session

```text
==========================================================================
Welcome to the calculator:

-> h to view history (last 5 operations)
-> c to clear history
-> r to set round off digits (e.g., 2 means 7.33)
-> enter expression like (1 + 1) to get an answer
-> q to quit program
==========================================================================

> 10 / 3
= 3.33

> 5 + 2
= 7.0

> h
--------History---------
-    5 + 2 = 7.0
-    10 / 3 = 3.33

