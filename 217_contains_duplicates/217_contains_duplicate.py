# Uses Dict - can keep track of how many times a number has been seen, uses more memory than Set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False

# Uses Set instead of Dict - faster/lower memory
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dict = set()

        for num in nums:
            if num in count_dict:
                return True
            count_dict.add(num)

        return False