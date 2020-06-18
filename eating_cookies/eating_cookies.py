'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    if n == 0: 
        return 1
    # First Fibonacci number is 0 
    elif n==1: 
        return 1
    # Second Fibonacci number is 1 
    elif n==2: 
        return 2
    elif n == 3:
        return 4

    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
