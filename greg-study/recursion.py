"""
Recursion general:
A base case is established as a stopping point.
When it is called, the program holds what it needs to do/calculate in memory until it hits the base case.
Once it reaches the base case, it starts to apply the actual values to each recursive calculation.

Fibonacci - the next number is the sum of the previous 2 numbers:
In this case, using 5 as an example, it is not 0 or 1 so:
I can output fib(5) once I know what fib(4) and fib(3) are (fib(n-1) + fib(n-2))
I can output fib(4) once I know what fib(3) and fib(2) are (fib(n-1) + fib(n-2))
I can output fib(3) once I know what fib(2) and fib(1) are (fib(n-1) + fib(n-2))
I can output fib(2) once I know what fib(1) and fib(0) are (fib(n-1) + fib(n-2))
I know what fib(1) and (0) are so I can go back up the chain
starting point [0, 1] fib(2) the next one will be 0 + 1 = *1* and the full sequence will be [0, 1, 1]
new starting point [0, 1, 1] fib(3) will be the sum of the result of fib(1) + fib(2) so will be 1 + 1 = *2* and the full sequence will be [0, 1, 1, 2]
new starting point [0, 1, 1, 2] fib(4) will be the sum of the result of fib(2) + fib(3) so will be 1 + 2 = *3* and the full sequence will be [0, 1, 1, 2, 3]
new starting point [0, 1, 1, 2, 3] fib(5) will be the sum of the result of fib(3) + fib(4) so will be 2 + 3 = *5* and the full sequence will be [0, 1, 1, 2, 3, 5]
"""


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))