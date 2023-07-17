
from members import add_member, display_members
from transactions_det import issue_book, return_book
from transactions import display_transactions
from books import add_book
from disp_books import display_books
class Library_management():
    def Process():
        while True:
            print("=== Library Management System ===")
            print("1. Add Book")
            print("2. Display Books")
            print("3. Add Member")
            print("4. Display Members")
            print("5. Issue Book")
            print("6. Return Book")
            print("7. Display Transactions")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                add_book()
            elif choice == "2":
                display_books()
            elif choice == "3":
                add_member()
            elif choice == "4":
                display_members()
            elif choice == "5":
                issue_book()
            elif choice == "6":
                return_book()
            elif choice == "7":
                display_transactions()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")


l=Library_management
l.Process()
