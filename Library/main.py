import json

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
    def __str__(self):
        return f"The book with title: {self.title} by {self.author} is {self.available}"

class LibraryManager:
    def __init__(self, filename = "library.json"):
        self.books=[]
        self.filename = filename
        self.load_data()
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book with title {title} was added to library")
    def search_book(self, query):
        found_book = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        if found_book:
            print("\n Search results: ")
            for book in found_book:
                print(book)
        else:
            print("\nBook not found...")
    def borrow_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower() and book.available:
                book.available = False
                print(f"You have borrowed '{book.title}'")
                return
        print(f"'{title}' is either not available or already borrowed.")
    def return_book(self, title):
        for book in self.books:
            if title.lower() == book.title.lower() and not book.available:
                book.available = True
                print(f"You have returned '{book.title}'")
                return
        print(f"'{title}' is either not borrowed or not in the libary.")
    def save_data(self):
        with open(self.filename, "w") as file:
            json_books = [{"title": book.title, "author": book.author,  "available": book.available} for book in self.books]
            json.dump(json_books, file, indent=4)
        print("Library data saved...")
    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                json_books = json.load(file)
                self.books = [Book(book["title"], book["author"], book["available"]) for book in json_books]
            print("Library data loaded...")
        except FileNotFoundError:
            print("No data file found. Starting with an empty library.")

def main():
    manager = LibraryManager()
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Save Data")
        print("6. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            manager.add_book(title, author)
        elif choice == 2:
            query = input("Enter book title or author to search: ")
            manager.search_book(query)
        elif choice == 3:
            title = input("Enter book title to borrow: ")
            manager.borrow_book(title)
        elif choice == 4:
            title = input("Enter book title to return: ")
            manager.return_book(title)
        elif choice == 5:
            manager.save_data()
        elif choice == 6:
            manager.save_data()
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()