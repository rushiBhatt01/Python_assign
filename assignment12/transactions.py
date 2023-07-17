def display_transactions():
    try:
        trans2=open("transactions_data.txt","+r")
        
        transactions = trans2.readlines()
        trans2.seek(0)

        if transactions:
            print("Transactions:")
            for transaction in transactions:
                transaction_type, book_id, member_id, date = transaction.split(",")
                print(f"Transaction Type: {transaction_type.strip()}, Book ID: {book_id.strip()}, Member ID: {member_id.strip()}, Date: {date.strip()}")
        else:
            print("No transactions found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")