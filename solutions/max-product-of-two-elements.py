from ast import literal_eval
import numpy as np
'''
Maximum Product of Two Elements in an Array

Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array
-------------------

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:
----------
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

Example 2:
----------
Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:
----------
Input: nums = [3,7]
Output: 12
 

Constraints:
------------
2 <= nums.length <= 500
1 <= nums[i] <= 10^3
'''

def maxProduct(nums):
    maxOutput = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            elif (nums[i]-1) * (nums[j]-1) > maxOutput:
                maxOutput = (nums[i]-1) * (nums[j]-1)
    return maxOutput

print("")
print("Maximum Product of Two Elements in an Array:")
print("")
print("Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array")
print("--------------------")
print("Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).")
print("")
print("Constraints:\n2 <= nums.length <= 500\n1 <= nums[i] <= 10^3")
print("")
print("Examples")
print("--------")
print(f"maxProduct([3,4,5,2]) => {maxProduct([3,4,5,2])}")
print(f"maxProduct([1,5,4,5]) => {maxProduct([1,5,4,5])}")
print(f"maxProduct([3,7]) => {maxProduct([3,7])}")
print("")
print("Try It Out!")
print("-----------")

example_nums = input("Input your own array of numbers:\t")
converted_nums = np.array(literal_eval(example_nums))

print("")
print(f"maxProduct({example_nums}) => {maxProduct(converted_nums)}")
print("")