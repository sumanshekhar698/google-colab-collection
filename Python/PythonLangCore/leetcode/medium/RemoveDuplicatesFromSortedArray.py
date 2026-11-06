class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]: # j: Iterates through the array to find unique elements.
                i += 1 # i: Keeps track of the position where the next unique element should be placed.
                nums[i] = nums[j] 

        return i + 1
    # 1,1,2,2,3