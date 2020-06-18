'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    # the sum i - n plus the nth Fibonacci number
    def Fibonacci(n): 
        if n<0: 
            print("Incorrect input") 
        # First Fibonacci number is 0 
        elif n==1: 
            return 0
        # Second Fibonacci number is 1 
        elif n==2: 
            return 1
        else: 
            return Fibonacci(n-1)+Fibonacci(n-2) 
    sum = Fibonacci(n) + n
    return sum


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 4

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
