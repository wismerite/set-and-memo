import mocks
import pytest
from set_or_memo import find_longest_word


def test_memo_compare_one_solution():
    assert (
        find_longest_word.find_longest_word(
            word_list=mocks.mock_one_solution_word_list, compare_type="memo"
        )
        == mocks.mock_one_solution_correct_answer
    )


def test_memo_compare_multiple_solutions():
    assert (
        find_longest_word.find_longest_word(
            word_list=mocks.mock_multiple_solutions_word_list, compare_type="memo"
        )
        == mocks.mock_multiple_solutions_correct_answer
    )


def test_memo_compare_no_solutions():
    with pytest.raises(Exception):
        find_longest_word.find_longest_word(
            word_list=mocks.mock_no_solutions_word_list, compare_type="memo"
        )
