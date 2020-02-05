# TO-DO: complete the helpe function below to merge 2 sorted arrays
testarr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


def merge(arrA, arrB):
    print('merge start')
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO

    idx_a = 0
    idx_b = 0
    # for i in range()

    while idx_a < len(arrA) and idx_b < len(arrB):
        if arrA[idx_a] <= arrB[idx_b]:

            merged_arr.append(arrA[idx_a])
            print(
                f'lhs < rhs - appending {arrA[idx_a]} merged_arr: {merged_arr} LHS: {arrA}, RHS {arrB}')
            idx_a += 1
            print(f'incrementing index a to {idx_a}')
        else:
            merged_arr.append(arrB[idx_b])
            print(
                f'rhs < lhs - appending {arrB[idx_b]} merged_arr: {merged_arr} LHS: {arrA}, RHS {arrB}')
            idx_b += 1
            print(f'incrementing index a to {idx_b}')

    merged_arr.extend(arrA[idx_a:])
    merged_arr.extend(arrB[idx_b:])
    print('merge end')
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    print('merge sort start')
    # TO-DO
    # break list in half until list length is 1
    #
    if len(arr) <= 1:
        print('length 1 merge sort stop')
        return arr

    else:
        half = len(arr) // 2
        lhs = merge_sort(arr[:half])
        rhs = merge_sort(arr[half:])
        print('lhs', lhs)
        print('rhs', rhs)
        print('merge sort stop... merging lhs & rhs')
        return merge(lhs, rhs)


print(merge_sort(testarr))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
