def get_book_text(filepath):
    # Opens the passed filepath and returns the contents as string
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    print(get_book_text("./books/frankenstein.txt"))

main()
