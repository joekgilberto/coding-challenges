from ast import literal_eval
import numpy as np

'''
Longest Common Prefix

Link: https://leetcode.com/problems/longest-common-prefix
----------------

Write a function to find the longest common prefix string amongst an array of strings.  If there is no common prefix, return an empty string "".



Example 1:
----------
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
----------
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:
------------
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

def longestCommonPrefix(strs):
    cache = ""
        
    for i in range(len(min(strs, key=len))+1):
        for j in range(len(strs)):
            if cache != strs[j][:i] and j == 0:
                cache = strs[j][:i]
            elif cache != strs[j][:i] and j > 0:
                cache = cache[:-1]
                break
                
        if len(cache) < i:
            break

    return cache

print("")
print("Longest Common Prefix:")
print("")
print("Link: https://leetcode.com/problems/longest-common-prefix")
print("----------------------")
print('Write a function to find the longest common prefix string amongst an array of strings.  If there is no common prefix, return an empty string "".')
print("")
print("Constraints:\n1 <= strs.length <= 200\n0 <= strs[i].length <= 200\nstrs[i] consists of only lowercase English letters.")
print("")
print("Examples")
print("--------")
print(f'longestCommonPrefix(["flower","flow","flight"]) => {longestCommonPrefix(["flower","flow","flight"])}')
print(f'longestCommonPrefix(["dog","racecar","car"]) => {longestCommonPrefix(["dog","racecar","car"])}')
print("")
print("Try It Out!")
print("-----------")

example_strs = input("Input your own array of numbers:\t")
converted_strs = np.array(literal_eval(example_strs))

print("")
print(f'longestCommonPrefix({converted_strs}) => "{longestCommonPrefix(converted_strs)}"')
print("")