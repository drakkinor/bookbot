from stats import get_num_words, get_char_counts, get_sorted_char_list
import sys

def get_book_text(filepath):
    # Opens the passed filepath and returns the contents as string
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Printing the 'report' with format defined here I guess?
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")

    words = get_num_words(get_book_text(sys.argv[1]))
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    
    char_counts = get_char_counts(get_book_text(sys.argv[1]))
    char_output = get_sorted_char_list(char_counts)
       
    for dictionary in char_output:
        for k, v in dictionary.items():
            print(f"{k}: {v}")
    
    print("============= END ===============")
    

main()
