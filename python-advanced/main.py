myfile = open("myfile.txt", "w")
myfile.write("Hello, World!\n")
myfile.write("This is a test file.\n")
myfile.close()
# Read the file and print its contents
with open("myfile.txt", "r") as myfile:
    contents = myfile.read()
    print(contents)
