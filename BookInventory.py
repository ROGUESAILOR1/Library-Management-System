import json
class BookInventory:
    def __init__(self,filename="books.json"):
        self.books = {}
        self.filename = filename
        try:
            self.json_loader(filename)
        except:
            print("No previous inventory found, starting with an empty inventory.")

    def add_book(self,book_id, book_title, author, total_copies):
        if book_id in self.books:
            self.books[book_id]["available_copies"] += 1
            self.books[book_id]["total_copies"] += 1
            print(f"{book_title} is already in stock, total copies updated")
        else:
            self.books[book_id]={
                "book_title": book_title,
                "author": author,
                "total_copies": total_copies,
                "available_copies": total_copies
            }
            print(f"{book_title} added successfully")

    def lend_book(self,book_id):
        if book_id in self.books and self.books[book_id]["available_copies"] > 0:
            self.books[book_id]["available_copies"] -= 1
            print("Book has been lent successfully")
        else:
            print("Book is not available for lending")
    def return_book(self,book_id):
        if book_id  in self.books and self.books[book_id]["available_copies"] < self.books[book_id]["total_copies"]:
            self.books[book_id]["available_copies"] += 1
            print("The Book has been returned successfully")
        elif self.books[book_id]["available_copies"] ==  self.books[book_id]["total_copies"]:
            print("Can't return the book, all copies are already present")
        else:print("Book ID not found in the inventory")
    def display_inventory(self):
        if not self.books:
            print("No books in inventory.")
        else:
            print("\nCurrent Inventory:")
            for book_id, info in self.books.items():
                print(f"ID: {book_id} | "
                  f"Title: {info['book_title']} | "
                  f"Author: {info['author']} | "
                  f"Total Copies: {info['total_copies']} | "
                  f"Available: {info['available_copies']}")
    def json_saver(self, filename="books.json"):
        with open(filename, "w") as f:
            json.dump(self.books, f, indent=4, separators=(", ", ": "))
        print("Data saved to JSON file successfully")
    def json_loader(self,filename="books.json"):
        with open(filename,"r") as f:
            self.books = json.load(f)
            return self.books