def file_inputs(file="student_info.txt"):
    try:
        f = open(file,"w")
        Roll_no=(input("enter roll number:"))
        name=(input("enter name:"))
        u_class=(input("enter class:"))
        f.writelines(Roll_no)
        f.writelines(name)
        f.writelines(u_class)
        f.seek(0)  
        print(f.readlines())
            
    except IOError:
        print("io error hint:Enter Input")

file_inputs()
