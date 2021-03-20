def nth_term(initial_term, common_ratio, term_number):
    return initial_term * common_ratio ** (term_number - 1)


def series(initial_term, common_ratio, term_number):
    if common_ratio != 1:
        return (initial_term * (1 - common_ratio ** term_number)) / (1 - common_ratio)

    else:
        return term_number * initial_term


def center_term(lef_side_term, right_side_term):
    return (lef_side_term * right_side_term) ** 0.5
