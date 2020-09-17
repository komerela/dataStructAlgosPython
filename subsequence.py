# Given two non-empty arrays of integers, write a function that determines whether
# the second array is a subsequence of the first one

# A subsequence of an array is a set of numbers that aren't necessary
# adjacent in the array but are in the same order as they appear in the subsequence

array = [5, 1, 22, 25, 6, -1, 8, 10]
subsequence = [1, 6, -1, 10]
""""
def isValidSubsequence(array, subsequence):
    subsequenceIdx = 0
    
    for value in array:
        if subsequenceIdx == len(subsequence):
            return True
        if subsequence[subsequenceIdx] == value:
            subsequenceIdx += 1
    subsequenceIdx == len(subsequence)
    
"""
def isValidSubsequence(array, subsequence):
    arrayIdx = subsequenceIdx = 0

    while arrayIdx < len(array) and subsequenceIdx < len(subsequence):
        if array[arrayIdx] == subsequence[subsequenceIdx]:
            subsequenceIdx += 1
        arrayIdx += 1
    return subsequenceIdx == len(subsequence)



S = isValidSubsequence(array, subsequence)
print(S)