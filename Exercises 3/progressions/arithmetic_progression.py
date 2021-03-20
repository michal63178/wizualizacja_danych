def nth_term(initial_term, term_number, common_difference):
    return initial_term + common_difference * (term_number - 1)


def series(initial_term, last_term, term_number):
    return (term_number * (initial_term + last_term)) / 2


def center_term(lef_side_term, right_side_term):
    return (lef_side_term + right_side_term) / 2
