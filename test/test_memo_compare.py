from set_or_memo import memo_compare, set_compare

def test_compare_one_solution():
    correct_answer = "bonke"
    assert memo_compare.find_longest_word_with_memo() == correct_answer
    assert set_compare.find_longest_word_with_set() == correct_answer


def test_compare_multiple_solutions():
    correct_answer = ["bonke", "monke"]
    assert memo_compare.find_longest_word_with_memo() == correct_answer
    assert set_compare.find_longest_word_with_set() == correct_answer
