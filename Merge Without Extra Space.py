# Link: https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        merged = arr1+arr2
        merged.sort()
        for i in range(n):
            arr1[i] = merged[i]
        for j in range(m):
            arr2[j] = merged[n + j]
