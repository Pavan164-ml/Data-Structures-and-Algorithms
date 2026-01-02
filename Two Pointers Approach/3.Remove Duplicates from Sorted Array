Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
# Bruteforce approach of using extra list to store the unique values and overwriting the main list with the unique values.
# TC : O(N)
# SC : O(N) --> Bad 
        unique_list = []
        for i in range(len(nums)):
            if nums[i] not in unique_list:
                # nums[i] = nums[i]
                unique_list.append(nums[i])
        
        for j in range(len(unique_list)):
            nums[j] = unique_list[j]

        return len(unique_list)

    # Two pointer approach 
        i = 0 # officer saab
        j = 1 # CM saab
        res = 1 # there will atleast 1 unique value 
        while(j<len(nums)):
            if(nums[j] == nums[j-1]):
                j+= 1
                continue
            nums[i+1] = nums[j]
            i+=1
            res+=1
            j+=1
        return res
