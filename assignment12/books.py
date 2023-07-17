
def add_book():
    try:
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        availability = True

        file=open("books_data.txt","+a")
        file.writelines(f"{book_id},{title},{availability}"+"\n")
        file.seek(0)
        
        print("Book added successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


