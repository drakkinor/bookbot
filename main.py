from stats import get_num_words

def get_book_text(filepath):
    # Opens the passed filepath and returns the contents as string
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    count = get_num_words(get_book_text("./books/frankenstein.txt"))
    print(f"{count} words found in the document")

main()
