# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615

# My first try
number = input("Enter an integer: ")
create_numbers = [0,1,2]
create_numbers[0] = number
create_numbers[1] = number * 2
create_numbers[2] = number * 3

result = int(create_numbers[0]) + int(create_numbers[1]) + int(create_numbers[2])

print(str(result))

# My second try
get_integer = input("Enter an integer: ")

number1 = get_integer
number2 = get_integer * 2
number3 = get_integer * 3

print(int(number1) + int(number2) + int(number3))

# My third try
get_integer = input("Enter an integer: ")
print(int(get_integer) + int(get_integer * 2) + int (get_integer * 3))