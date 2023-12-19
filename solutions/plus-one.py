from ast import literal_eval
import numpy as np
'''
Plus One

Link: https://leetcode.com/problems/plus-one
--------

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
 

Example 1:
----------
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
----------
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
----------
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
'''

def plusOne(digits):
    last = len(digits) - 1

    if digits[last] == 9:
        for i in range(last,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        
        if digits[0] == 0:
            digits.insert(1,0)
    else:
        digits[last] = digits[last] + 1

    return digits

# Specific function is compatible with numpy import
def numpyPlusOne(strDigits):
    digits = np.array(literal_eval(strDigits))
    last = len(digits) - 1

    if digits[last] == 9:
        for i in range(last,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                break
        
        if digits[0] == 0:
            digits=np.insert(digits, 0, 1)
    else:
        digits[last] = digits[last] + 1

    return digits

print("")
print("Plus One:")
print("")
print("Link: https://leetcode.com/problems/plus-one")
print("--------")
print("You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.")
print("")
print("Constraints:\n1 <= digits.length <= 100\n0 <= digits[i] <= 9\ndigits does not contain any leading 0's.")
print("")
print("Examples")
print("--------")
print(f"plusOne([1,2,3]) => {plusOne([1,2,3])}")
print(f"plusOne([4,3,2,1]) => {plusOne([4,3,2,1])}")
print(f"plusOne([1,9]) => {plusOne([1,9])}")
print("")
print("Try It Out!")
print("-----------")

example_digits = input("Input your own array of numbers:\t")

print("")
print(f"plusOne({example_digits}) => {numpyPlusOne(example_digits)}")
print("")