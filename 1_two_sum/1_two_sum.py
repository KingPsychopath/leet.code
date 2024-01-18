
# (One-pass Hash Table)
# Time complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found

# Same as above but with comments and better variable names
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the numbers we've seen and their indices
        seen = {}

        # Iterate over the list
        for index, num in enumerate(nums):
            # Calculate the number we're looking for
            complement = target - num

            # If we've seen the complement before, return its index and the current index
            if complement in seen:
                return [seen[complement], index]

            # Otherwise, add the current number and its index to the dictionary
            seen[num] = index

        # If we've gone through the entire list and haven't found a pair of numbers that sum to the target,
        # return an indication that no solution was found
        return []


# Brute force solution
# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]