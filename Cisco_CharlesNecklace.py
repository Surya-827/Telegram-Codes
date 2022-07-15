# Read only region start
class Solution(object):
    @classmethod
    def find_Sol(cls, input1, input2, input3):
        '''
        input1 = int
        input2 = int
        input3 = int

        Expected return type : int
        '''
        # Read only region end
        # Write code here

        N = input1
        L = input2
        R = input3

        dp = [[0 for i in range(R - L + 1)]
              for i in range(N)]

        result = 0
        for i in range(N):
            dp[i][0] = 1
        for i in range(1, len(dp[0])):
            dp[0][i] = dp[0][i - 1] + 1

        result = dp[0][R - L]
        for i in range(1, N):

            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

            result += dp[i][R - L]

        return result if result > 0 else -1


if __name__ == "__main__":
    obj = Solution()

    input1 = int(input())
    input2 = int(input())
    input3 = int(input())

    print(obj.find_Sol(input1, input2, input3))
