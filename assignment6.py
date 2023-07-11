def ds(roll_no, name):
    
    mylist = [roll_no, name]
    print("List:", mylist)
    my_tuple = (roll_no, name)
    print("Tuple:", my_tuple)
    myset = {roll_no, name}
    print("Set:", myset)
    mydict = {'roll_no': roll_no, 'name': name}
    
    mylist[0] = 12345
    print("List:", mylist)
    my_tuple = (119, "rushi")
    print("Tuple:", my_tuple)
    myset.remove(roll_no)
    myset.add(609)
    print("Set:", myset)
    mydict['name'] = "adad"
    print("Dictionary:", mydict)
    
    del mylist
    print("List:", mylist)  
    del my_tuple
    print("Tuple:", my_tuple) 
    del myset
    print("Set:", myset) 
    del mydict
    print("Dictionary:", mydict) 

ds(12345, "Rushi Bhatt")
