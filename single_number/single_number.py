'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # new list
    new_list = []

    # iterate through arr
    for num in range(len(arr)):
    # if not new list, append - pop
        if arr[num] not in new_list:
            new_list.append(arr[num])
        elif arr[num] in new_list:
            new_list.remove(arr[num])

    # return remaining number in new list
    return new_list[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")