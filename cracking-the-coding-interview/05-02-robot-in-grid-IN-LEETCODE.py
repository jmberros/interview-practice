# Robot in a Grid: Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right. LeetCode

https://leetcode.com/problems/unique-paths-ii/description/


#
# 20 10 4 1
# 10 6  3 1
# 4  3  2 1
# 1  1  1 Y
#
# 6 2 X 1
# 4 2 1 1
# 2 1 X 1
# 1 1 1 1

# . 1 1
# . X 1
# . . 1
#

# R = 3, C = 3
# dp(0, 0): dp(0, 1) + dp(1, 0) = 2
#    dp(0, 1): dp(0, 2) + dp(1, 1) = 1
#      dp(0, 2): dp(0, 3) + dp(1, 2) = 1
#        dp(0, 3): 0
#        dp(1, 2): dp(1, 3) + dp(2, 2) = 1
#          dp(1, 3): 0
#          dp(2, 2): 1
#      dp(1, 1): 0
#    dp(1, 0): dp(1, 1) + dp(2, 1) = 1
#      dp(1, 1): 0  # Cached!
#      dp(2, 1): dp(2, 2) + dp(3, 1) = 1
#        dp(2, 2): 1  # Cached!
#        dp(3, 1): 0


def print_matrix(m):
    for row in m:
        print(row)
    print("--")


class Solution:
    # Bottom-up solution. Just reverse the path: the number of possible ways to
    # go from start to end is the same as the number of ways of going from
    # end to start. Now you can only go up and left ;)
    # This is more memory-expensive
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        num = [[0] * C for _ in range(R)]


        for row in range(R):
            for col in range(C):
                if obstacleGrid[row][col] == 1:  # Obstacle here
                    num[row][col] = 0
                    continue

                if row == 0 and col == 0:  # Base case
                    num[row][col] = 1
                    continue

                if row == 0 and col > 0:  # Top row
                    num[row][col] = num[row][col-1]
                    continue

                if col == 0 and row > 0:  # Left col
                    num[row][col] = num[row-1][col]
                    continue

                num[row][col] = num[row-1][col] + num[row][col-1]

                # print_matrix(num)

        return num[R-1][C-1]


    # Top-down, recursion + memoization approach
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        def dp(row, col, memo):
            if row >= R or col >= C or obstacleGrid[row][col] == 1:
                return 0
            if row == R - 1 and col == C - 1:
                return 1

            key = f"R{row}C{col}"
            if key not in memo:
                memo[key] = dp(row, col + 1, memo) + dp(row + 1, col, memo)

            return memo[key]


        return dp(0, 0, {})
