
def display_books():
    try:
        src = open("books_data.txt","+r")
        books=src.readlines()
        src.seek(0)

        if books:
            print("Books:")
            for book in books:
                book_id, title, availability = book.split(",")
                print(f"Book ID: {book_id.strip()}, Title: {title.strip()}, Availability: {availability.strip()}")
        else:
            print("No books found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")