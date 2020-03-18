"""still not working"""


def count_inversion_quad(A):
    inv_count = 0
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                inv_count += 1
    return inv_count


def count_inv_aux(left_part, right_part):
    inv_count = 0
    left_index = 0
    right_index = 0
    for i in range((len(left_part) + len(right_part)) - 1):
        if left_index == len(left_part):
            break
        if right_index == len(right_part):
            break

        if left_part[left_index] <= right_part[right_index]:
            inv_count += 1
            left_index += 1
        else:
            inv_count += 1
            right_index += 1

    return inv_count


def count_inversion_opt(A):
    start_index = 0
    end_index = len(A)
    if end_index == 1:
        return 0
    middle_index = (len(A) - start_index) // 2
    left_part_count = count_inversion_opt(A[start_index:middle_index])
    right_part_count = count_inversion_opt(A[middle_index:end_index])
    inv = count_inv_aux(A[:middle_index], A[middle_index:]) + left_part_count + right_part_count

    return inv


array_4 = [1, 3, 2, 4, 5, 8, 10, 7, 9]
array_worst_15 = [6, 5, 4, 3, 2, 1]
count_inv = count_inversion_opt(array_worst_15)
print(count_inv)
