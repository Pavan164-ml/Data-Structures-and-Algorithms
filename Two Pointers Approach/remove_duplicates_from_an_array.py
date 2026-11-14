# Refer to written notes
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        officer = 0 
        cm = 1 
        n = len(nums)
        unique_elements = 1
        while(cm<n):
            if(nums[cm] == nums[cm-1]):
                cm +=1
                continue
            nums[officer+1] = nums[cm]
            officer += 1
            cm += 1
            unique_elements += 1
        return unique_elements

  https://leetcode.com/problems/remove-duplicates-from-sorted-array/
