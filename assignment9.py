# operations.py

class CException(Exception):
    pass

def file_operations(filename, mode):
    try:
        file = open(filename, mode)
        print(f"File '{filename}' opened ")
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: I/O error occurred.")

def calculate(num):
    if num < 0:
        raise CException("Error: Square root of a negative number is undefined.")
    return num ** 0.5

def split_string(string, ):
    return string.split()
