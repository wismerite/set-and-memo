import mocks
from set_or_memo import set_compare


def test_set_compare_one_solution():
    assert (
        set_compare.find_longest_word_with_set(
            word_list=mocks.mock_one_solution_word_list
        )
        == mocks.mock_one_solution_correct_answer
    )


def test_set_compare_multiple_solutions():
    assert (
        set_compare.find_longest_word_with_set(
            word_list=mocks.mock_multiple_solutions_word_list
        )
        == mocks.mock_multiple_solutions_correct_answer
    )
