Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
# Bruteforce approach of using extra list to store the unique values and overwriting the main list with the unique values.
 
# Preparing the unique list using an extra list 
        # unique_list = []
        # for i in range(len(nums)):
        #     if nums[i] not in unique_list:
        #         unique_list.append(nums[i])
        
# Storing the unique list back to original list, it might still have values beyond k but that will be ignored
        # for j in range(len(unique_list)):
        #     nums[j] = unique_list[j]

        # return len(unique_list)
# TC : O(N)
# SC : O(N) --> Bad



# Two pointer approach - To rearrange the values 
        i = 0 # officer saab
        j = 1 # CM saab
        res = 1 # there will atleast 1 unique value
        # CM saab that is jth index tries to find the unique element so that he can assign a house to them.
        # If at all the previous number is same as current then he will simply skip the assignment and move on to next.
        # Lets say there are no diplicates given at all then the array will remain as is without any modifications as per current logic.
        #  
        while(j<len(nums)): #Q Why not len(nums)-1 > Because we want to traverse all elements to check for duplicates before assigning the house.
            if(nums[j] == nums[j-1]):
                j+= 1
                continue
            nums[i+1] = nums[j] #If there is no duplicate found at all , this will overwrite the index with the same value as it previously had as i and j will be same here.
            i+=1 # Incrementing already sorted list
            res+=1 # Incrementing the unique values found
            j+=1 # Incrementing to the next index of unprocessed list
        return res 
        
