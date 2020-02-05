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
    # set swap to true at start to ensure while statement runs
    swap_occurred = True
    # amount of passes needed to run through all possible iterations
    possible_passes = len(arr) - 1
    # possible passes remaining and a swap occurred
    while possible_passes > 0 and swap_occurred:
        # reset swap to false before for loop runs
        swap_occurred = False
        # run for loop for each possible pass
        for i in range(possible_passes):
            # if RHS is less than LHS then swap and set swapped to true
            # if swapped is true then while statement continues
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_occurred = True
        # shorten possible passes by 1 as index increases
        possible_passes = possible_passes - 1
    # if no passes possible OR a swap did not occur(meaning order correct) return array
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
