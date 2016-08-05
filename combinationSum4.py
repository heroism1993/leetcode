#!/bin/python

class Solution():
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(len(nums)==0):
            if(target==0):
                return 1
            else:
                return 0

        last=nums.pop()
        tmpTarget=target
        count=0
        while ( tmpTarget >= 0 ):
            count+=self.combinationSum4(nums,tmpTarget)
            tmpTarget-=last

        nums.append(last)
        return count

if(__name__=="__main__"):
    nums=[1,2]
    target=3
    solution=Solution()
    print solution.combinationSum4(nums,target)