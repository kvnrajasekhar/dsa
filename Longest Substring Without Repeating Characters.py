class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ref=[]
        temp=0
        prev=temp
        if s== " ":
            return 1
        for i in s:
            while(i in ref):
                ref.pop(0)
                temp-=1
                
            else:
                ref.append(i)
                temp+=1
                prev=max(prev,temp)
        return prev
