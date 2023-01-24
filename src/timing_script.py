from set_or_memo.find_longest_word import find_longest_word
from time import time

words = open("words.txt", "r")
word_list = words.readlines()
words.close()

compare_types = ["set", "memo"]
num_iterations = 10

for compare_type in compare_types:
    # it would certainly be possible to just define num_iterations here, but
    # assigning "num_iterations" to "runs_left" here improves readability
    # for both the loop and by keeping script configs together near the top.
    runs_left = num_iterations
    start = time()
    while runs_left > 0:
        find_longest_word(word_list=word_list, compare_type=compare_type)
        runs_left -= 1
    end = time()
    print(
        f"{compare_type} took {end - start} seconds to complete {num_iterations} iterations."
    )
