# Import the regular expression module
import re

# Define the LibraryManagementSystem class
class LibraryManagementSystem:
    
    # Constructor method to initialize the list of books
    def __init__(self):
        self.books = []

    # Method to add a book to the library
    def add_book(self):
        try:
            # Prompt user to enter book information
            print("Add Book Information:")
            book_id = input("Enter book ID: ")
            
            # Validate the format of book ID using regular expression
            if not re.match("^[0-9]{4}$", book_id):
                raise ValueError("Invalid book ID format. Please use #### format.")
            title = input("Enter book title: ")
            author = input("Enter author's name: ")
            genre = input("Enter book genre: ")
            available_copies = int(input("Enter number of available copies: "))
            self.books.append({"book_id": book_id, "title": title, "author": author, "genre": genre, "available_copies": available_copies})
            print("Book added successfully!")
        except ValueError as e:
            print(e)

    # Method to view all books in the library
    def view_books(self):
        if self.books:
            print("Book List:")
            for book in self.books:
                
                # Print details of each book
                print(f"Book ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Available Copies: {book['available_copies']}")
        else:
            print("No books in the library.")

    def search_book(self):
        try:
            # Prompt user for search criteria
            criteria = input("Enter search criteria (Book ID / Title / Author / Genre): ").lower()
            
            # Validate search criteria
            if criteria not in ["book id", "title", "author", "genre"]:
                raise ValueError("Invalid search criteria.")
            search_query = input(f"Enter {criteria}: ").lower()

            found_books = []
            
            # Iterate through the list of books to find matching books
            for book in self.books:
                if search_query in book[criteria.replace(" ", "_")]:
                    found_books.append(book)

            if found_books:
                
                # Display matching books
                print("Matching Books:")
                for book in found_books:
                    print(f"Book ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Available Copies: {book['available_copies']}")
            else:
                print("No books found matching the criteria.")
        except ValueError as e:
            print(e)

    def update_book(self):
        try:
            # Prompt user for the book ID to update  
            book_id = input("Enter the book ID to update: ")
            for book in self.books:
                if book['book_id'] == book_id:
                    
                    # Update book information
                    book['title'] = input("Enter updated book title: ")
                    book['author'] = input("Enter updated author's name: ")
                    book['genre'] = input("Enter updated book genre: ")
                    book['available_copies'] = int(input("Enter updated number of available copies: "))
                    print("Book information updated successfully.")
                    return
            print("Book not found.")
        except ValueError:
            print("Invalid number of available copies. Please enter a valid integer.")

    def delete_book(self):
        try:
            # Prompt user for the book ID to delete
            book_id = input("Enter the book ID to delete: ")
            for book in self.books:
                if book['book_id'] == book_id:
                    
                    # Remove the book from the list
                    self.books.remove(book)
                    print("Book deleted successfully.")
                    return
            print("Book not found.")
        except ValueError:
            print("Invalid input.")

    def check_availability(self):
        try:
            # Prompt user for the book ID
            book_id = input("Enter book ID: ")
            for book in self.books:
                if book['book_id'] == book_id:
                    
                    # Display available copies of the book
                    print(f"Available copies of Book {book['book_id']} ({book['title']}): {book['available_copies']}")
                    return
            print("Book not found.")
        except ValueError:
            print("Invalid input.")

    def issue_book(self):
        try:
            # Prompt user for the book ID to issue
            book_id = input("Enter book ID: ")
            for book in self.books:
                if book['book_id'] == book_id:
                    num_copies = int(input("Enter number of copies to issue: "))
                    if num_copies <= book['available_copies']:
                        
                        # Reduce available copies of the book
                        book['available_copies'] -= num_copies
                        print(f"{num_copies} copies issued successfully for Book {book['book_id']} ({book['title']}).")
                    else:
                        print("Insufficient copies available.")
                    return
            print("Book not found.")
        except ValueError:
            print("Invalid input.")

    def return_book(self):
        try:
            # Prompt user for the book ID to return
            book_id = input("Enter book ID: ")
            for book in self.books:
                if book['book_id'] == book_id:
                    num_copies = int(input("Enter number of copies to return: "))
                    
                    # Increase available copies of the book
                    book['available_copies'] += num_copies
                    print(f"{num_copies} copies returned successfully for Book {book['book_id']} ({book['title']}).")
                    return
            print("Book not found.")
        except ValueError:
            print("Invalid input.")

    def display_library(self):
        if self.books:
            # Display the library catalog
            print("Library Catalog:")
            for book in self.books:
                print(f"Book ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, Available Copies: {book['available_copies']}")
        else:
            print("No books in the library.")
            
    # Methods for searching, updating, deleting, checking availability, issuing, returning, and displaying the library catalog follow a similar structure        
            
    # Method to display the menu of options for the user
    def display_menu(self):
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book Information")
        print("5. Delete Book")
        print("6. Check Book Availability")
        print("7. Issue Book")
        print("8. Return Book")
        print("9. Display Library")
        print("10. Exit")
        
    # Main method to run the library management system
    def main(self):
        while True:
            # Display the menu
            self.display_menu()
            
            # Prompt user for choice
            choice = input("Enter your choice: ")

            try:
                if choice == '1':
                    self.add_book()
                elif choice == '2':
                    self.view_books()
                elif choice == '3':
                    self.search_book()
                elif choice == '4':
                    self.update_book()
                elif choice == '5':
                    self.delete_book()
                elif choice == '6':
                    self.check_availability()
                elif choice == '7':
                    self.issue_book()
                elif choice == '8':
                    self.return_book()
                elif choice == '9':
                    self.display_library()
                elif choice == '10':
                    print("Thank you for using the Library Management System.")
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
            except Exception as e:
                print("An error occurred:", e)

# Check if the script is being run directly
if __name__ == "__main__":
    
    # Create an instance of LibraryManagementSystem
    system = LibraryManagementSystem()
    
    # Call the main method to start the program
    system.main()
