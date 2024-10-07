def filter_sort_factors_3_7(ls):
    factors_ls = []
    not_factors_ls = []

    for v in ls:
        if v > 0:
            if v % 3 == 0 or v % 7 == 0:
                factors_ls.append(int(v))
            else:
                not_factors_ls.append(v)

    factors_ls.sort()
    not_factors_ls.sort(reverse=True)

    return [factors_ls, not_factors_ls]