class Solution(object):

    @classmethod
    def getLength(cls, s: str) -> int:
        stack = []
        n = len(s)

        for i in range(n):
            stack.push(s[i])

            while 1:
                if len(stack) > 1:
                    ch1 = stack.top()
                    stack.pop()
                    ch2 = stack.top()
                    stack.pop()

                    x = ch1 - '0'
                    y = ch2 - '0'

                    if (x + y == 17):
                        continue
                    else:
                        stack.push(ch2)
                        stack.push(ch1)
                        break
                else:
                    break
        return len(stack) + 1


if __name__ == "__main__":
    obj = Solution()
    s = input()
    print(obj.getLength(s))
