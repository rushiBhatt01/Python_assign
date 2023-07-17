

def issue_book():
    try:
        book_id = input("Enter book ID: ")
        member_id = input("Enter member ID: ")
        date = input("Enter date (DD-MM-YYYY): ")

        trans=open("transactions_data.txt","+at")
        trans.writelines( f"Issue,{book_id},{member_id},{date}"+"\n")
        trans.seek(0)
        
        print("Book issued successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def return_book():
    try:
        book_id = input("Enter book ID: ")
        member_id = input("Enter member ID: ")
        date = input("Enter date (DD-MM-YYYY): ")

        trans=open("transactions_data.txt","+a")
        trans.writelines( f"return,{book_id},{member_id},{date}"+"\n")
        trans.seek(0)
        
        print("Book returned successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


