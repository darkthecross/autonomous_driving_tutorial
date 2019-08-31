def infinite_fib(n):
    # if n == 1 or n == 0:
    #    return 1
    return infinite_fib(n-1) + infinite_fib(n-2)
print(infinite_fib(100))