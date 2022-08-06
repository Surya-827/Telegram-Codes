from functools import partial

def curry(fn, *args):

  return partial(fn, *args)

Examples:

add = lambda x, y: x + y

add10 = curry(add, 10)

add10(20) # 30
