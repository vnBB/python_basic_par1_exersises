# 7. Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java
filename = str(input("Enter a filename with extension: "))
extension = filename.split(".", -1)
print(str(extension[1]))