from book import Book

def main():
    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    price = float(input("Enter Book Price: "))

    b1 = Book(book_id, title, author, price)

    print("\n--- Book Details ---")
    b1.display()

main()
