def min_in_list(lst):
    first_min_number = lst[0]

    for i in lst:
        if i < first_min_number:
            first_min_number = i
    return first_min_number


english_score = [33, 44, 55, 66, 77]

result = min_in_list(english_score)
print(result)
