from stats import get_num_words, get_char_counts, get_sorted_char_list

def get_book_text(filepath):
    # Opens the passed filepath and returns the contents as string
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    #words = get_num_words(get_book_text("./books/frankenstein.txt"))
    #print(f"{words} words found in the document")
    char_count = get_char_counts(get_book_text("./books/frankenstein.txt"))
    get_sorted_char_list(char_count)

main()
