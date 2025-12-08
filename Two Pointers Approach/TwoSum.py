class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
