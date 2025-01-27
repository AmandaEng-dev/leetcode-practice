class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #target = target, nums = list, result will be list

        #iterate through the list
        for i in range (len(nums)):
        #iterate through the list with a second value to compare the first iteratiomn too
            for j in range (i+1, len(nums)):
                #if a finds b and adds them and it is the target, return answer
                #if not, goes back top to iterate to the the next a value
                if nums[i] + nums[j] == target:
                    return [i,j];
                


            
        

    
            

        