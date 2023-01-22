from typing import Union


def find_longest_word_with_memo(word_list: list) -> Union[str, list]:
    longest_words = [""]
    for word in word_list:
        word_len = len(word)
        if has_repeating_characters(word):
            continue
        if word_len > len(longest_words[0]):
            longest_words = [word]
            continue
        elif word_len == len(longest_words[0]):
            longest_words.append(word)

    if longest_words == "":
        raise Exception("word list has no words without repeating characters")
    elif len(longest_words) == 1:
        return longest_words[0]
    else:
        return longest_words


def has_repeating_characters(word: str) -> bool:
    word = sorted(word)
    memo = {word.pop(): 1}
    for i in range(1, word.len()):
        if word.pop() in memo:
            return False
    return True
