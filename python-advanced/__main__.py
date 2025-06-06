from .file_helper import read_file, say_hello, write_to_file


def main():
    print("This is the main function of the project.")
    say_hello()


if __name__ == "__main__":
    print("Running project...")
    main()
    write_to_file()
    read_file()
