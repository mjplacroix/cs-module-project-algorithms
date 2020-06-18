'''
Input: an integer
Returns: an integer
'''
import sys 
def eating_cookies(n, cache=None):
    if cache is None:
        cache = {}
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
    elif cache and cache[n]:
        return cache[n]
    else:
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

# print(eating_cookies(10, {}))