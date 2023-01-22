from typing import Union


def find_longest_word_with_set(word_list: list) -> Union[str, list]:
    longest_words = [""]
    for word in word_list:
        word_len = len(word)

        # check for repeating chars
        if word_len > len(set(word)):
            continue
        # no repeating chars, so see if it's the longest word
        elif word_len > len(longest_words[0]):
            longest_words = [word]
            continue
        elif word_len == len(longest_words[0]):
            longest_words.append(word)

    if longest_words == "":
        raise Exception("word list has no words with non-repeating characters")
    elif len(longest_words) == 1:
        return longest_words[0]
    else:
        return longest_words
