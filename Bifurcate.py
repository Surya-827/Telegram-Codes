

Splits values into two groups, based on the result of the given filtering function.

👉Use a list comprehension to add elements to groups, based on the value returned by fn for each element.

👉If fn returns a truthy value for any element, add it to the first group, otherwise add it to the second group.

CODE:

def bifurcate_by(lst, fn):

  return [

    [x for x in lst if fn(x)],

    [x for x in lst if not fn(x)]

  ]

Examples

Input:

bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')

Output:

[ ['beep', 'boop', 'bar'], ['foo'] ]



