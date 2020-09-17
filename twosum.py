# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 9

def twoNumberSum(array, targetSum):
   

    if array is None and len(array) < 2 and targetSum is None:
        return []
    # Iterate through array to the before last value of the array
    for i in range(len(array) - 1):
        first_num = array[i]
        # Iterate through all the rest of numbers in the array
        for j in range(i + 1, len(array)):
            second_num = array[j]
            if first_num + second_num == targetSum:
        # To print all combinations
        # print("(", first_num, ", ", second_num, ")", sep="")
                return [first_num, second_num]

    return []


array = [3, 4, 6, -4, 5, -2, 1]
targetSum = 9

S = twoNumberSum(array, targetSum)
print(S)

"""
class Solution():
    def twoNumberSum(self, array, targetSum):
        numbers = {}

        for num in numbers:
            match = targetSum - num
            if match in numbers:
                return [match, num]

            else:
                numbers[num] = True
        return []


S = Solution()

print(S.twoNumberSum( array, targetSum))
"""