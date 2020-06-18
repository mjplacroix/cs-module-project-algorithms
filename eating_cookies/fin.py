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
  
# Driver Program 
  
print(Fibonacci(9)) 
# ------------------------------------------------------------------------
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
# ------------------------------------------------------------------------
def rec_fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return rec_fib(n-1) + rec_fib(n-2)

print(rec_fib(25))
# ------------------------------------------------------------------------

cache = {0:1, 1:1}
def cache_fib(n):
    if n in cache:
        return cache[n]

    cache[n] = cache_fib(n-1) + cache_fib(n-2)

    return cache[n]

print(cache_fib(80))