# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        while cur_index >= 1 and arr[smallest_index] < arr[cur_index-1]:
            temp = arr[cur_index]
            arr[cur_index] = arr[cur_index - 1]
            arr[cur_index-1] = temp
            cur_index -= 1

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr)):
        while i >= 1 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

    return arr


testarr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(bubble_sort(testarr))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
