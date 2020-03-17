def merge(left_part, right_part):
    merged_array = [0] * (len(left_part) + len(right_part))

    left_part.append(float("inf"))
    right_part.append(float("inf"))

    left_index = 0
    right_index = 0
    for i in range(len(merged_array)):
        if left_part[left_index] <= right_part[right_index]:
            merged_array[i] = left_part[left_index]
            left_index += 1
        else:
            merged_array[i] = right_part[right_index]
            right_index += 1

    return merged_array


def merge_sort(array_to_sort):
    """что то неправильно с рекурсией"""
    start_index = 0
    end_index = len(array_to_sort)
    if end_index == 1:
        return array_to_sort[:1]
    middle_index = (len(array_to_sort) - start_index) // 2
    left_part = merge_sort(array_to_sort[start_index:middle_index])
    right_part = merge_sort(array_to_sort[middle_index:end_index])
    sorted_array = merge(left_part, right_part)

    return sorted_array


unsorted_array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
result_array = merge_sort(unsorted_array)
print(result_array)
