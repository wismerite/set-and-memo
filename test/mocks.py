mock_one_solution_word_list = ["beep", "bonke"]
mock_one_solution_correct_answer = "bonke"

mock_multiple_solutions_word_list = ["beep", "bonke", "monke"]
mock_multiple_solutions_correct_answer = ["bonke", "monke"]

# no "correct answer" for list with no solutions because pytest expects an exception rather than a return value
mock_no_solutions_word_list = ["beep", "booop"]
