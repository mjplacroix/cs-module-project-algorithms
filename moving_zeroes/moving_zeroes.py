'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    new_list = []

    # iterate through the list
    for num in range(len(arr)):
    # if number is zero, continue
        if arr[num] == 0:
            new_list.append(arr[num])
    # if number is not zero, insert at beginning of list
        if arr[num] != 0:
            new_list.insert(0, arr[num])

    return new_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")