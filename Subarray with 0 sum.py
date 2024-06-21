# link : https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1
class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        #Your code here
        #Return true or false
        hashmap = set()
        total = 0
        for i in arr:
            total += i
            if total==0 or total in hashmap:
                return True
            else:
                hashmap.add(total)
        return False
