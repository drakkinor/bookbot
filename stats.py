def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_char_counts(text):
    # returns dictionary of all detected characters and their counts in order characters appear
    char_list = list(text.lower())
    #print(char_list)
    char_counts = {}
    for item in char_list:
        char_counts[item] = char_counts.get(item, 0) + 1
    #char_counts = dict(sorted(char_counts.items()))
    #print(char_counts)
    return char_counts

def get_sorted_char_list(dictionary):
    #returns a list of dictionaries of all alpha characters in order of highest count
   
    #sorting the input dictionary by value and creating a new dictionary with the results
    sorted_dict = dict(sorted(dictionary.items(), reverse=True, key=lambda x:x[1]))
    #print(sorted_dict)

    #instantiate return list
    sorted_list = []

    #iterate sorted dictionary to create and append new single-entry dictionaries for each kv pair
    #filters for alpha chars only, may have been better to separate that functionality?
    for item in sorted_dict:
        if item.isalpha():
            mydict = {}
            mydict[item] = sorted_dict[item]
            sorted_list.append(mydict)
    
    #print(sorted_list)
    return sorted_list

    