# Function to add a new book to the library
def add_book(library, title, author, genre):
    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "availability": True
    }
    library.append(book)
    print("Book added successfully!")

# Function to remove a book from the library
def remove_book(library, title):
    for book in library:
        if book["title"] == title:
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Function to search for books by title or author
def search_book(library, search_query):
    found_books = []
    for book in library:
        if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower():
            found_books.append(book)
    if found_books:
        print("Found books:")
        for book in found_books:
            print_book(book)
    else:
        print("No books found.")

# Function to display all available books
def display_books(library):
    if library:
        print("Available books:")
        for book in library:
            if book["availability"]:
                print_book(book)
    else:
        print("Library is empty.")

# Function to print book details
def print_book(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Availability: {'Available' if book['availability'] else 'Not Available'}")

# Main function to run the library management system
def main():
    library = []  # List to store books

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Available Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            add_book(library, title, author, genre)
        elif choice == "2":
            title = input("Enter title of the book to remove: ")
            remove_book(library, title)
        elif choice == "3":
            search_query = input("Enter title or author to search: ")
            search_book(library, search_query)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

# Run the main function
if __name__ == "__main__":
    main()


