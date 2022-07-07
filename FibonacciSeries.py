//Python

Fibonacci Number using Recursion

CODE:

def fib(n):

  if n <= 0: # base case 1

    return 0

  if n <= 1: # base case 2

    return 1

  else: # recursive step

    return fib(n-1) + fib(n-2)

Fibonacci Number using Dynamic Programming:

  

CODE:

 calculated = {}

def fib(n):

  if n == 0: # base case 1

    return 0

  if n == 1: # base case 2

    return 1

  elif n in calculated:

    return calculated[n]

  else: # recursive step

    calculated[n] = fib(n-1) + fib(n-2)

    return calculated[n]

