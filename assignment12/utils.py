def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")

def read_from_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data
