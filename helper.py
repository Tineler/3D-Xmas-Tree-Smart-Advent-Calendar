def is_december(date):
    return date.month == 12


def is_between_christmas_eve_and_new_year(date):
    return is_december(date) and 25 <= date.day
