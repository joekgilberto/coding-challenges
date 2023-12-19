'''
Longest Substring Without Repeating Characters

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters
----------------------------------------------

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:
----------
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
----------
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
----------
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
------------
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

def lengthOfLongestSubstring(s):
    cache = []
    chars = list(s)
    longest = 0

    for char in chars:
        if char not in cache:
            cache.append(char)
            if len(cache)>longest:
                longest = len(cache)
        else:
            idx = cache.index(char)
            sliced = slice(idx+1,len(cache))
            cache = cache[sliced]
            cache.append(char)

    return longest

print("")
print("Longest Substring Without Repeating Characters:")
print("")
print("Link: https://leetcode.com/problems/longest-substring-without-repeating-characters")
print("--------")
print("Given a string s, find the length of the longest substring without repeating characters.")
print("")
print("Constraints:\n0 <= s.length <= 5 * 104\ns consists of English letters, digits, symbols and spaces.")
print("")
print("Examples")
print("--------")
print(f"lengthOfLongestSubstring('abcabcbb') => {lengthOfLongestSubstring('abcabcbb')}")
print(f"lengthOfLongestSubstring('bbbbb') => {lengthOfLongestSubstring('bbbbb')}")
print(f"lengthOfLongestSubstring('pwwkew') => {lengthOfLongestSubstring('pwwkew')}")
print("")
print("Try It Out!")
print("-----------")

example_str = input("Input your own string:\t")

print("")
print(f"lengthOfLongestSubstring({example_str}) => {lengthOfLongestSubstring(example_str)}")
print("")