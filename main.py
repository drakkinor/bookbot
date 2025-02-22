def get_book_text(filepath):
    # Opens the passed filepath and returns the contents as string
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    word_list = []
    #print(word_list)
    word_list = text.split()
    #print(word_list)
    return len(word_list)
    #pass


def main():
    count = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{count} words found in the document")

main()
