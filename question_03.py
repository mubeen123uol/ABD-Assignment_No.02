
from typing import List


class Library:

    def __init__(self, name: str):
        self.name: str = name
        self.books: List[str] = []  # Collection stored as a list of strings

    def add_book(self, book: str) -> None:
        if not book or not book.strip():
            print("[Warning] Book title cannot be empty.")
            return

        clean_title = book.strip()
        self.books.append(clean_title)
        print(f"[Success] Added '{clean_title}' to '{self.name}'.")

    def remove_book(self, book_title: str) -> bool:
        clean_title = book_title.strip()
        if clean_title in self.books:
            self.books.remove(clean_title)
            print(f"[Success] Removed '{clean_title}' from '{self.name}'.")
            return True
        else:
            print(f"[Error] '{clean_title}' is not found in '{self.name}'.")
            return False

    def search_book(self, keyword: str) -> List[str]:
        query = keyword.strip().lower()
        matching_books = [book for book in self.books if query in book.lower()]
        return matching_books

    def display_books(self) -> None:
        print(f"\n--- Books in '{self.name}' Collection ---")
        if not self.books:
            print("The library collection is currently empty.")
        else:
            for index, book in enumerate(self.books, start=1):
                print(f"  {index}. {book}")
        print("-" * (len(self.name) + 30))


def main():
    print("=" * 65)
    print("           ASSIGNMENT 02 - QUESTION # 03 SOLUTION           ")
    print("=" * 65)

    # 1. Instantiate the Library
    my_library = Library("City Central Library")
    print(f"Created new library instance: '{my_library.name}'")

    # 2. Add books to the library collection
    print("\n--- Adding Books ---")
    my_library.add_book("Python Crash Course")
    my_library.add_book("Fluent Python")
    my_library.add_book("Clean Code")
    my_library.add_book("Introduction to Algorithms")
    my_library.add_book("Automate the Boring Stuff with Python")
    my_library.add_book("Design Patterns")

    # 3. Display all books
    my_library.display_books()

    # 4. Search for books by keyword
    search_terms = ["Python", "Code", "Database"]
    print("\n--- Searching for Books ---")
    for term in search_terms:
        matches = my_library.search_book(term)
        print(f"Search keyword: '{term}' -> Matches found ({len(matches)}): {matches}")

    # 5. Remove books
    print("\n--- Removing Books ---")
    my_library.remove_book("Clean Code")         # Existing book
    my_library.remove_book("Unknown Book")       # Non-existing book

    # 6. Display books after removal
    print("\n--- Collection After Updates ---")
    my_library.display_books()

    print("=" * 65)


if __name__ == "__main__":
    main()
