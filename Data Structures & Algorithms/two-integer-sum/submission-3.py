class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={} #val -> ind
        for i,n in enumerate(nums):
            indices[n]=i

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in indices and indices[difference]!=i:
                return [i,indices[difference]]
        return []
            

            
    

        
        