Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

**Example 1:**

**Input:** nums = [2,7,11,15], target = 9
**Output:** [0,1]
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]

**Example 3:**

**Input:** nums = [3,3], target = 6
**Output:** [0,1]

"""
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Brute force with a double for loop is possible but not optimal -> (O(n^2)) Time Complexity  
To Improve run-time we need a way to check if a number is in the list in O(1) time -> Hash Set
So we are trading space for speed

# Approach
<!-- Describe your approach to solving the problem. -->
- Used a set at first but changed to dictionary to keep track of the frequency of each element
- Enumerated list to keep track of the index of each element
- Calculated target - element to find the other element needed to add up to target
- Check if the other element is in the dictionary and if it is, check if the index of the other element is not the same as the index of the current element
- If all those checks pass we've found it

# Complexity
- Time complexity:
O(n) - We iterate over the array once.
- Space complexity:
O(n) - We use a hash set to store at most n number of elements.
"""