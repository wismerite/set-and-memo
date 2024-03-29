from typing import Union


def find_longest_word(word_list: list, compare_type: str) -> Union[str, list]:
    longest_words = [""]

    if compare_type not in ["set", "memo"]:
        raise Exception(f"invalid compare type requested: {compare_type}")
    check_for_repeating_chars = {
        "set": lambda word: len(word) > len(set(word)),
        "memo": _has_repeating_characters,
    }

    for word in word_list:
        # check for repeating chars
        if check_for_repeating_chars[compare_type](word):
            continue
        # no repeating chars, so see if it's the longest word
        word_len = len(word)
        if word_len > len(longest_words[0]):
            longest_words = [word]
            continue
        elif word_len == len(longest_words[0]):
            longest_words.append(word)

    if longest_words[0] == "":
        raise Exception("word list has no words without repeating characters")
    elif len(longest_words) == 1:
        return longest_words[0]
    else:
        return longest_words


def _has_repeating_characters(word: str) -> bool:
    word = list(word)
    while len(word) > 0:
        char = word.pop()
        if char in word:
            return True
    return False
