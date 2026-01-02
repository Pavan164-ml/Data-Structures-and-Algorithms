class Solution(object):
    def sortedSquares(self, nums):
         # Brute force first square the number then sort it 
        # T: OnLog(N) --> Worst
        # S: O(N) --> Very bad
        arr = [] # Initializing an extra array to store the squares
        for i in range(len(nums)):
            arr.append(nums[i]*nums[i])
        arr.sort() # sorting the squared array so negative values will be handled as well.
        return arr
        
        # 2 pointer approach
        pos = []
        neg = []
        n = len(nums)
        for i in range(n):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        # case 1 all are postive values
        res = []
        if len(neg)==0:
            for i in range(n):
                res.append(nums[i]*nums[i])
            return res
        # case 2 all are negative values  
        if len(pos)==0:
            for i in range(n):
                res.append(nums[i]*nums[i])
            res.reverse()
            return res

        # case 3 if list has both +ve and -ve values
        neg.reverse()
        x = len(pos)
        y = len(neg) 
        i = j = 0 # assigning all index to 0  
        # inserting the records to res list in ascending order 
        while(i<x and j<y):
            if(pos[i]*pos[i]<neg[j]*neg[j]):
                res.append(pos[i]*pos[i])
                i+=1
            else:
                res.append(neg[j]*neg[j])
                j+=1
        # it is possible that neg and pos arrays are of not the same size so we handle each of these subsenarios individually
        while(j<y):
            res.append(neg[j]*neg[j])
            j+=1
        while(i<x):
            res.append(pos[i]*pos[i])
            i+=1
        return res

# Absolutely genius approach
# class Solution(object):
    # def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        idx = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[idx] = nums[left] * nums[left]
                left += 1
            else:
                res[idx] = nums[right] * nums[right]
                right -= 1
            idx -= 1

        return res
