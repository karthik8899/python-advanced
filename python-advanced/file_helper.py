def say_hello():
    print("Hello, from greet function!")


def write_to_file():
    with open("output.txt", "w") as file:
        file.write("This is a sample output file.\n")
        file.write("It contains some text data.\n")
        file.close()


# Read the file and print its contents
def read_file():
    with open("output.txt", "r") as file:
        contents = file.read()
        print(contents)
