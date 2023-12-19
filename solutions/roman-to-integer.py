'''
Roman to Integer

Link: https://leetcode.com/problems/roman-to-integer
----------------

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:
----------
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
----------
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
----------
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:
------------
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

def romanToInt(s):
    romans = [*s.upper()]
    total = 0

    def nextIs(idx,letter):
        if idx+1 < len(romans) and romans[idx+1] == letter:
            return True
        else:
            return False

    def beforeIs(idx,letter):
        if idx+1 < len(romans) and romans[idx-1] == letter:
            return True
        else:
            return False

    for idx, letter in enumerate(romans):
        if letter == "I":
            if nextIs(idx,"V") or nextIs(idx,"X"):
                continue
            else:
                total = total + 1
        elif letter == "V":
            if beforeIs(idx,"I"):
                total = total + 4
            else:
                total = total + 5
        elif letter == "X":
            if nextIs(idx,"L") or nextIs(idx,"C"):
                continue
            elif beforeIs(idx,"I"):
                    total = total + 9
            else:
                total = total + 10
        elif letter == "L":
            if beforeIs(idx,"X"):
                total = total + 40
            else:
                total = total + 50
        elif letter == "C":
            if nextIs(idx,"D") or nextIs(idx,"M"):
                continue
            elif beforeIs(idx,"X"):
                total = total + 90
            else:
                total = total + 100
        elif letter == "D":
            if beforeIs(idx,"C"):
                    total = total + 400
            else:
                total = total + 500
        elif letter == "M":
            if beforeIs(idx,"C"):
                total = total + 900
            else:
                total = total + 1000

    return total

print("")
print("Roman to Integer:")
print("")
print("Link: https://leetcode.com/problems/roman-to-integer")
print("-----------------")
print("Given a roman numeral, convert it to an integer.")
print("")
print("Constraints:\n1 <= s.length <= 15\ns contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').\nIt is guaranteed that s is a valid roman numeral in the range [1, 3999].")
print("")
print("Examples")
print("--------")
print(f"romanToInt('III') => {romanToInt('III')}")
print(f"romanToInt('LVIII') => {romanToInt('LVIII')}")
print(f"romanToInt('MCMXCIV') => {romanToInt('MCMXCIV')}")
print("")
print("Try It Out!")
print("-----------")

example_str = input("Input your own valid roman numeral:\t")
converted_str = example_str.upper()

print("")
print(f"romanToInt({example_str.upper()}) => {romanToInt(example_str.upper())}")
print("")