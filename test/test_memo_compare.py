import mocks
from set_or_memo import memo_compare


def test_memo_compare_one_solution():
    assert (
        memo_compare.find_longest_word_with_memo(
            word_list=mocks.mock_one_solution_word_list
        )
        == mocks.mock_one_solution_correct_answer
    )


def test_memo_compare_multiple_solutions():
    assert (
        memo_compare.find_longest_word_with_memo(
            word_list=mocks.mock_multiple_solutions_word_list
        )
        == mocks.mock_multiple_solutions_correct_answer
    )
