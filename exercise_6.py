# 6. Write a Python program which accepts a sequence of comma-separated numbers 
# from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

data = input("Enter a sequence of comma-separated numbers: ")

list_data = list(data.split(", "))
tuple_data = tuple(data.split(", "))

print("List: " + str(list_data))
print("Tuple: " + str(tuple_data))