#NotImplemented
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ans=list()
        len1=len(nums1)
        len2=len(nums2)
        if(len1==0 or len2==0):
            return ans
        flag1=0
        flag2=0
        flag1plus2=0
        flag2plus1=0
        plused_num1=[0]*(len1+1)
        plused_num2=[0]*(len2+1)
        
        while(k>0):
            if(flag2==len2 and flag1==len1):
                break
            if(flag2plus1==len1):
                flag2+=1
                flag2plus1=plused_num2[flag2]
                continue
            if(flag1plus2==len2):
                flag1+=1
                flag1plus2=plused_num1[flag1]
                continue
            if(flag1==flag2plus1 and flag2==flag1plus2):
                ans.append([nums1[flag1],nums2[flag2]])
                k-=1
                flag1plus2+=1
                flag2plus1+=1
                continue
            if(nums1[flag1]+nums2[flag1plus2]>nums1[flag2plus1]+nums2[flag2]):
                ans.append([nums1[flag2plus1],nums2[flag2]])
                k-=1
                plused_num1[flag2plus1]=flag2+1
                flag2plus1+=1
            else:
                ans.append([nums1[flag1],nums2[flag1plus2]])
                k-=1
                plused_num2[flag1plus2]=flag1+1
                flag1plus2+=1
        
        return ans

if(__name__=="__main__"):
    nums1=[1,2,3]
    nums2=[4,5,6]
    count=30
    solution=Solution()
    print solution.kSmallestPairs(nums1,nums2,count)