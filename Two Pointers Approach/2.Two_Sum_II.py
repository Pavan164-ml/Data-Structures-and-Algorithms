class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # numbers.sort() # not required as the array is already sorted  
        left, right = 0 , len(numbers) - 1 # assigning left and right indexes

        while left<right: # we only run the loop until left index remains less than the right 
            current_sum = numbers[left] + numbers[right] # sum of left and right index 
            if current_sum == target : 
                # the sum must be equal to the target and also the numbers should not be the same  
                return [left+1,right+1] # if sum is matched return the associated indexes + 1 
            elif current_sum<target: #if sum is less than the target the we increase the left so
                left+=1
            else: # if sum is greater than the target then we need to decrease right 
                right-=1
        return None
