strs = ["eat","tea","tan","ate","nat","bat", "rate"]

class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        new_list = None
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
        new_list = list(anagrams.values())
        return new_list

    
S = Solution()

print(S.groupAnagrams(strs))