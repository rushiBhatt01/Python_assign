
num = []
for i in range(5):
    number = int(input("Enter a number: "))
    num.append(number)
print(num)

print("Sum of all numbers:", sum(num))
print("Smallest number:", min(num))
print("Largest number:", max(num))
print("ascending order:", sorted(num))
print("descending order:", sorted(num, reverse=True))
num_tuple = tuple(num)
print("converted to a tuple:", num_tuple)
del num
print("List deleted.")
