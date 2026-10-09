# Advanced Back-End Development (CS02338|11) - Assignment #02
**The University of Lahore | Department of Technology**

This repository contains the complete solutions for Assignment #02 of Advanced Back-End Development.

---

## Repository Contents

- `question_01.py`: Operations on integer lists using functions:
  - `remove_duplicates(numbers)`: Returns a new list with duplicates removed while preserving original order.
  - `find_average(numbers)`: Returns the average of all numbers in the list.
  - `multiply_by_scalar(numbers, scalar)`: Multiplies each element by a scalar value.
- `question_02.py`: Store inventory management using loops:
  - Iterates through store inventory dictionary and prints each item with its quantity.
  - Calculates and prints the total value of inventory (`quantity * price`).
- `question_03.py`: Object-Oriented Library Management System:
  - `class Library`:
    - `__init__(self, name)`: Initializes library with a name and stores books in a list of strings.
    - `add_book(self, book)`: Adds a book to the collection.
    - `remove_book(self, book_title)`: Removes a book from the collection.
    - `search_book(self, keyword)`: Searches for matching book titles by keyword.
    - `display_books(self)`: Displays all books currently in the collection.
- `main.py`: Unified runner executing all questions sequentially.

---

## How to Run

Run the unified runner:
```bash
python main.py
```

Or run individual questions:
```bash
python question_01.py
python question_02.py
python question_03.py
```
