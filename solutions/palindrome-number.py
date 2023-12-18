'''
Palindrome Number

Link: https://leetcode.com/problems/palindrome-number
----------------------------------------------

Given an integer x, return true if x is a palindrome, and false otherwise.
 


Example 1:
----------
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
----------
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
----------
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:
------------
-231 <= x <= 231 - 1
'''

def isPalindrome(x):
    forward = str(x)
    reverse = str(x)[::-1]

    if forward == reverse:
        return True
    else:
        return False

print("")
print("Palindrome Number:")
print("")
print("Link: https://leetcode.com/problems/palindrome-number")
print("--------")
print("Given an integer x, return true if x is a palindrome, and false otherwise.")
print("")
print("Constraints:\n0 <= s.length <= 5 * 104\ns consists of English letters, digits, symbols and spaces.")
print("")

print(f"isPalindrome(121) => {isPalindrome(121)}")
print(f"isPalindrome(-121) => {isPalindrome(-121)}")
print(f"isPalindrome(10) => {isPalindrome(10)}")
print("")