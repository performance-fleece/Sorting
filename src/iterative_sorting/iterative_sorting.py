# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        while cur_index >= 1 and arr[cur_index] < arr[cur_index-1]:
            temp = arr[cur_index]
            arr[cur_index] = arr[cur_index - 1]
            arr[cur_index-1] = temp
            cur_index -= 1

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    swap_occurred = True
    remaining_passes = len(arr) - 1
    while remaining_passes > 0 and swap_occurred:
        swap_occurred = False
        for i in range(remaining_passes):
            if arr[i+1] < arr[i]:
                swap_occurred = True
                arr[i+1], arr[i] = arr[i], arr[i+1]
        remaining_passes = remaining_passes - 1
    return arr


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    for i in range(len(arr)):
        low_value_idx = i
        for test_idx in arr[i+1::]:
            if arr[test_idx] < arr[low_value_idx]:
                low_value_idx = test_idx
        arr[i], arr[low_value_idx] = arr[low_value_idx], arr[i]

    return arr
