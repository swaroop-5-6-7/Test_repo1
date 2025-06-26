class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.lend_data = {}
        self.attendance = {}

    def display_books(self):
        print(f"\nBooks available in {self.name}:")
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added to the library.")

    def lend_book(self, user, book_name):
        if book_name not in self.books:
            print(f"Book '{book_name}' not found in the library.")
        elif book_name in self.lend_data:
            print(f"Book is already lent to {self.lend_data[book_name]}.")
        else:
            self.lend_data[book_name] = user
            print(f"Book '{book_name}' lent to {user}.")

    def return_book(self, book_name):
        if book_name in self.lend_data:
            self.lend_data.pop(book_name)
            print(f"Book '{book_name}' returned successfully.")
        else:
            print(f"Book '{book_name}' was not lent out.")

    def mark_attendance(self, user):
        if user in self.attendance:
            self.attendance[user] += 1
        else:
            self.attendance[user] = 1
        print(f"Attendance marked for {user}. Days present: {self.attendance[user]}")

    def view_attendance(self):
        print("\nAttendance Records:")
        if not self.attendance:
            print("No attendance records found.")
        else:
            for user, days in self.attendance.items():
                print(f"{user}: {days}")


def main():
    library = Library("Central Library")

    while True:
        print("\nLibrary Menu")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Mark Attendance")
        print("6. View Attendance")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            book_name = input("Enter the name of the book to add: ")
            library.add_book(book_name)
        elif choice == '3':
            user = input("Enter your name: ")
            book_name = input("Enter the name of the book to lend: ")
            library.lend_book(user, book_name)
        elif choice == '4':
            book_name = input("Enter the name of the book to return: ")
            library.return_book(book_name)
        elif choice == '5':
            user = input("Enter your name to mark attendance: ")
            library.mark_attendance(user)
        elif choice == '6':
            library.view_attendance()
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
