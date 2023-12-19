from ast import literal_eval
import numpy as np
'''
Number of Good Pairs

Link: https://leetcode.com/problems/number-of-good-pairs
-------------------

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:
----------
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
----------
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
----------
Input: nums = [1,2,3]
Output: 0
 

Constraints:
------------
1 <= nums.length <= 100
1 <= nums[i] <= 100
'''

def numIdenticalPairs(nums):
    good_pairs = 0;
    for i in range(0, len(nums)):
        for j in range(0,i):
            if nums[i] == nums[j]:
                good_pairs += 1

    return good_pairs

print("")
print("Number of Good Pairs:")
print("")
print("Link: https://leetcode.com/problems/number-of-good-pairs")
print("--------------------")
print("Given an array of integers nums, return the number of good pairs.  A pair (i, j) is called good if nums[i] == nums[j] and i < j.")
print("")
print("Constraints:\n1 <= nums.length <= 100\n1 <= nums[i] <= 100")
print("")
print("Examples")
print("--------")
print(f"numIdenticalPairs([1,2,3,1,1,3]) => {numIdenticalPairs([1,2,3,1,1,3])}")
print(f"numIdenticalPairs([1,1,1,1]) => {numIdenticalPairs([1,1,1,1])}")
print(f"numIdenticalPairs([1,2,3]) => {numIdenticalPairs([1,2,3])}")
print("")
print("Try It Out!")
print("-----------")

example_nums = input("Input your own array of numbers:\t")
converted_nums = np.array(literal_eval(example_nums))

print("")
print(f"numIdenticalPairs({example_nums}) => {numIdenticalPairs(converted_nums)}")
print("")