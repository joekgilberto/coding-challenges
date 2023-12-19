from ast import literal_eval
import numpy as np
'''
Majority Element II

Link: https://leetcode.com/problems/plus-one
-------------------

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:
----------
Input: nums = [3,2,3]
Output: [3]

Example 2:
----------
Input: nums = [1]
Output: [1]

Example 3:
----------
Input: nums = [1,2]
Output: [1,2]
 

Constraints:
------------
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
'''

def majorityElement(nums):
    returnArr = []
    minOccurance = (len(nums) / 3)

    for i in range(len(nums)):
        count = 0;
        for j in range(i, len(nums)):
            if nums[j] == nums[i]:
                count += 1
        
        if count > minOccurance and nums[i] not in returnArr:
            returnArr.append(nums[i])

    return returnArr;

print("")
print("Majority Element II:")
print("")
print("Link: https://leetcode.com/problems/majority-element-ii")
print("--------------------")
print("Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.")
print("")
print("Constraints:\n1 <= nums.length <= 5 * 104\n-109 <= nums[i] <= 109")
print("")
print("Examples")
print("--------")
print(f"majorityElement([3,2,3]) => {majorityElement([3,2,3])}")
print(f"majorityElement([1]) => {majorityElement([1])}")
print(f"majorityElement([1,2]) => {majorityElement([1,2])}")
print("")
print("Try It Out!")
print("-----------")

example_nums = input("Input your own array of numbers:\t")
converted_nums = np.array(literal_eval(example_nums))

print("")
print(f"majorityElement({example_nums}) => {majorityElement(converted_nums)}")
print("")