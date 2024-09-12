'''hw2_debugging.py'''
import rand


def merge_sort(arr):
    '''Merge sort function'''
    # Remove None values from the array
    arr = [x for x in arr if x is not None]

    if not arr:  # Handle empty arrays
        return []

    if len(arr) == 1:
        return arr

    half = len(arr) // 2
    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    '''Recombine function'''
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(left_index, len(left_arr)):
        merge_arr[i + right_index] = left_arr[i]

    for i in range(right_index, len(right_arr)):
        merge_arr[i + left_index] = right_arr[i]

    return merge_arr


arr1 = rand.random_array([None] * 20)
arr_out = merge_sort(arr1)

print(arr_out)
