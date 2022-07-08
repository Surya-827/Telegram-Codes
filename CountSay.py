class Solution:

    def countAndSay(self, n: int) -> str:

	    if n == 1:		    return "1"

	    else:

		    string = self.countAndSay(n - 1)

		    count  = 0

		    ret    = []

		    cur    = string[0]

		    for char in string:

			    if char != cur:

				    ret.append("%i%c" % (count, cur))

				    cur = char

				    count = 1

			    else:

				    count += 1

		    ret.append("%i%c" % (count, cur))

		    return "".join(ret)
