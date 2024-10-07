def count_factors_3_7(ls):
    count = 0
    for v in ls:
        if v % 3 == 0 or v % 7 == 0:
            count += 1

    return count

def filter_factors_3_7(ls):
    factors_ls = []
    not_factors_ls = []

    for v in ls:
        if v > 0:
            if v % 3 == 0 or v % 7 == 0:
                factors_ls.append(int(v))
            else:
                not_factors_ls.append(v)

    return [factors_ls, not_factors_ls]