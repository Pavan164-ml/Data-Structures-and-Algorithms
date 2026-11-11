Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


### Bruteforce
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # Brute force
        for i in range(len(numbers)): # We need to see all the elements
            required = target - numbers[i] # calculates the difference to find in the list
            for j in range(i+1,len(numbers)): # we dont need to start from 0 because there is no point in goin back we would have already done that comparison given the array is sorted
                if numbers[j] == required:
                    return i+1,j+1 # because it is not expecting 0 based index as return type instead want the positional numbers
        


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # Bruteforce approach using 2 loops by finding all possible combinations
        for i in range(len(nums)):
            j = i+1
            for j in range(len(nums)):
                if ( i!=j and nums[i] + nums[j] == target):
                    print(i,j)
                    return i,j

# 1. only 2 numbers are to be found  
# 2. lets say we already have the first number as of i'th index 
# 3. we just need to find out the next number which could be at jth index
# 4. This is by taversing the entire array at 2 scale 
# 5. At each step checking if the sum of ith and jth index elements match the target or not
# Correction I had missed the edge case where i th index and jth index shouldnt be same as it would make no sense. So after that submission was perfect
# Need to optimize the time complixity from O(N2)


# Hashmap Approach
# SC : O(N)
# TC : O(N)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Map that holds #value and index

        for i,num in enumerate(nums): # iterates through each index and the actual value of the list 
            check = target - num # checks if the difference between target and current number is present in the list. If yes then we will return.
            if check in seen:
                return [seen[check],i] # this will only return the index not the number, because hashmap key is number and value is index here 
            seen[num]= i  # if the difference is not present we add the key as number and value as current index for future iterations
        return None # if the loop is completed and we dont find any answes then there is no result

# nums = [2, 7, 11, 15]
# target = 9

# Iteration 1
# i = 0
# num = 2

# - check = 9 - 2 = 7
# - Is 7 in seen? No. Dictionary is empty.
# - Execute seen[2] = 0.
# seen = {2: 0}


# Iteration 2
# i = 1
# num = 7

# - check = 9 - 7 = 2
# - Is 2 in seen? Yes!
# - Execute return [seen[2], 1].
# Result
# [0, 1]

# In the above approach lets say we have x+y = target 
# x is the ith element; y = target - x
# Using hashmap we try to find out the y value and dont care which index it is present at;
# Only way is to check it in the hasmap and return if the difference is found in HM.


link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2 pointer approach without using any extra space
        i = 0 
        j = len(numbers)-1
        while(i < len(numbers)):
            if(numbers[i]+numbers[j]==target):
                return i+1,j+1
            elif(numbers[i]+numbers[j]<target):
                i+=1
            else:
                j-=1
        return None

