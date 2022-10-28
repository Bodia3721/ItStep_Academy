def rec_sum_list(l: list):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + rec_sum_list(l[1:])
