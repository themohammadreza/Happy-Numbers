def happy_number(number, tried_once=None):
    if tried_once is None:
        tried_once = []

    if number == 1:
        pass
    if number in tried_once:
        pass