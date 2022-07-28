def authentication(n):

    if n % 3 == 0 and n % 5 == 0:

        return 'FizzBuzz'

    elif n % 3 == 0:

        return 'Fizz'

    elif n % 5 == 0:

        return 'Buzz'

    else:

        return str(n)

print("\n".join(authentication(n) for n in range(1, 21)))

Python3 ✅🤞🙂
