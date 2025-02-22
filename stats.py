def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_char_counts(text):
    char_list = list(text.lower())
    #print(char_list)
    char_counts = {}
    for item in char_list:
        char_counts[item] = char_counts.get(item, 0) + 1
    char_counts = dict(sorted(char_counts.items()))
    #print(char_counts)
    return char_counts
  