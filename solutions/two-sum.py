from ast import literal_eval
import numpy as np

'''
Two Sum

Link: https://leetcode.com/problems/two-sum
--------

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.  You may assume that each input would have exactly one solution, and you may not use the same element twice.  You can return the answer in any order.

 

Example 1:
----------
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
----------
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
----------
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
------------
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

def twoSum(nums, target):
    for i, num in enumerate(nums):
        for j in range(i+1,len(nums)):
            sum = num + nums[j]
            if sum == target:
                return [i,j]

print("")
print("Two Sum:")
print("")
print("Link: https://leetcode.com/problems/two-sum")
print("--------")
print("Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.  You may assume that each input would have exactly one solution, and you may not use the same element twice.  You can return the answer in any order.")
print("")
print("Constraints:\n2 <= nums.length <= 104\n-109 <= nums[i] <= 109\n-109 <= target <= 109\nOnly one valid answer exists.")
print("")
print("Examples")
print("--------")
print(f"twoSum([2,7,11,15], 9) => {twoSum([2,7,11,15], 9)}")
print(f"twoSum([3,2,4], 6) => {twoSum([3,2,4], 6)}")
print(f"twoSum([3,3], 6) => {twoSum([3,3], 6)}")
print("")
print("Try It Out!")
print("-----------")

example_nums = input("Input your own array of numbers:\t")
converted_nums = np.array(literal_eval(example_nums))
example_target = input("Input your own target number:\t")
converted_target = int(example_target)

print("")
print(f"twoSum({example_nums}, {example_target}) => {twoSum(converted_nums, converted_target)}")
print("")
