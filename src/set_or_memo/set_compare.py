def find_longest_word_with_set(word_list:list) -> str:
    longest_word = ""
    for word in word_list:
        word_len = len(word)

        # check for repeating chars
        if word_len > len(set(word)):
            continue
        # no repeating chars, so see if it's the longest word
        elif word_len > len(longest_word):
            longest_word = word
            continue


    if longest_word == "":
        raise Exception("word list has no words with non-repeating characters")
    else:
        return longest_word
    