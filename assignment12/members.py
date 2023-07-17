import utils

def add_member():
    try:
        member_id = input("Enter member ID: ")
        name = input("Enter member name: ")

        stc=open("members_data.txt", "+at")
        stc.writelines(f"{member_id},{name}"+"\n")
        stc.seek(0)
        
        print("Member added successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def display_members():
    try:
        memb = open("members_data.txt","+r") 
        members=memb.readlines()
        memb.seek(0)
        if members:
            print("Members:")
            for member in members:
                member_id, name = member.split(",")
                print(f"Member ID: {member_id.strip()}, Name: {name.strip()}")
        else:
            print("No members found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
