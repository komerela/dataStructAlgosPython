# Given (input) 2d matrix of ascending rows and columns,
# find the K (input)th smallest number (output)

# A = [[1, 2, 5],
#  [1, 4, 8]]

# B = [[ 3, 6, 8],
#      [ 4, 7, 9]]
#

# Input: 0, A
# Output: 1

# Input: 1, A | 1, B
# Output: 1,  |  4

# Input: 2, A | 2, B
# Output: 2   | 6

# Assign the first row to a variable
# Traverse the rows

import heapq

matrix = [[1, 2, 5]]


def kth_smallest_number(matrix, k):
    min_heap = A[0]

    heapq.heapify( min_heap )

    for row in matrix[1:]:
        for num in row:
            heapq.heappush( min_heap, num )

    k_smallest_list = heapq.nsmallest( k, min_heap )

    return k_smallest_list[-1]


print( "1st: " + str( kth_smallest_number( matrix, 3 ) ) )

# 1. Clarify the problem
# 2. Define your approach
# 3. Propose a solution
# 4. Consider any additional information or constraints
# 5. Propose alternative solution
# 6. Implement the solution

# Input: A 2d array AND some integer K
# Is K zero-indexed or K 1-indexed?
# What does ascending mean?

# VALID
# A = [ 1 2 3 4 ], k = 3

# INVALID
# [ 1 2 3 5 ]
# [ 2 2 2 4 ]

# VALID
# [ 1 2 3 4 5 ]
# [ 1 2 3 4 5 ]
# [ 2 3 4 5 6 ]
# k = 5 --> 3

- [1] -> [2] -> [3] -> [4] -> [5]
- |.|.|.|.|
- [1].->.[2]
_ >.[3]. ->[4] -> [5]
- |.|.|.|.|
- [2] -> [3] -> [4]  ->[4] -> [6]

# For any given (a,b), you know that (a-1, b-1)
# is <= (a,b)
# likewise, you know (a, b-1) is <= (a,b)
# ...
# using these facts, you may be able to come up with a different solution than the min-heap solution

# for square (4,3), there 14 squares <= it
# if K <= 14, we don't ever have to look at (4,3)

# for square (3,3) there are 8 squares <= it.


# Min-heap
# Min-heaps help us maintain a list of things where you can pop off the smallest number

# OK I don't know how to solve this, but... I can brute force it!
# I can just add everything to an array, and then sort it.

# I know that that takes,
# O(|A| + |A|log|A| + K) = O(|A|log|A|)

# We want you to know
# How to solve the problem, at-depth
# WHY you solve it this way
# How good your solution is
# How your solution compares to other solutions

# Space-time complexity


# Here are two alternative binray search methods


# public class Solution {
#     public int kthSmallest(int[][] matrix, int k) {
#         int lo = matrix[0][0], hi = matrix[matrix.length - 1][matrix[0].length - 1] + 1;//[lo, hi)
#         while(lo < hi) {
#             int mid = lo + (hi - lo) / 2;
#             int count = 0,  j = matrix[0].length - 1;
#             for(int i = 0; i < matrix.length; i++) {
#                 while(j >= 0 && matrix[i][j] > mid) j--;
#                 count += (j + 1);
#             }
#             if(count < k) lo = mid + 1;
#             else hi = mid;
#         }
#         return lo;
#     }
# }

# Let's say you get points for interviews
# And... there are communication points, technical knowledge points, and problem points

# If you never talk or document your code, you get 0 communication points
# If you don't solve the problem successfully, you'll get less problem points
# If you have no solution at all, you get 0 problem points

# But if you have a weak solution, but communicated well, and documented well, you'll still get many points