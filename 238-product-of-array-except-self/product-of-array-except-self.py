class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n=len(nums)
        # res=[0]*n
        # for i in range(n):
        #     add=1
        #     for j in range(n):
        #         if j==i:
        #             continue
        #         else:
        #             add*=nums[j]
        #     res[i]=add
        # return res

        # prod,zero_count=1,0
        # for num in nums:
        #     if num:
        #         prod*=num
        #     else:
        #         zero_count+=1

        # if zero_count>1:
        #     for i in range(len(nums)):
        #         return [0]*len(nums)
        
        # res=[0]*len(nums)

        # for i,c in enumerate(nums):
        #     if zero_count==1:
        #         res[i]=0 if c!=0 else prod
        #     else:
        #         res[i]=prod//c    
        # return res

        # not optimized
        # elif zero_count==1:
        #     for num in nums:
        #         if num==0:
        #             res.append(prod)
        #         else:
        #             res.append(0)
        #     return res        
        # else:
        #     for num in nums:
        #         res.append(prod//num)
        # return res
        # n=len(nums) 
        # pre=[0]*n
        # suf=[0]*n
        # res=[0]*n
        
        # pre[0]=suf[n-1]=1
        # for i in range(1,n):
        #     pre[i]=pre[i-1]*nums[i-1]
        # for i in range(n-2,-1,-1):
        #     suf[i]=nums[i+1]*suf[i+1]
        
        # for i in range(n):
        #     res[i]=pre[i]*suf[i]
        # return res 

        n=len(nums) 
        res=[1]*n
        
        prefix=1
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1    
        for i in range(n-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res    






                    


        