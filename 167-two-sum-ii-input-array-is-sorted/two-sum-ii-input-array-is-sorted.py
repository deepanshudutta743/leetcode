class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # res=[]
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             res.append(i+1)
        #             res.append(j+1)
        #             return res
        # return res
        res=[]
        for i in range(len(numbers)):
            temp=target-numbers[i]
            left=i+1
            right=len(numbers)-1
            while left<=right:
                mid=left+(right-left)//2
                if numbers[mid]==temp:
                    return [i+1,mid+1]
                elif numbers[mid]<temp:
                    left=mid+1
                else:
                    right=mid-1
        return []                    


        