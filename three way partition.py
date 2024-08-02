#link:https://www.geeksforgeeks.org/problems/three-way-partitioning/1
class Solution:
	def threeWayPartition(self, array, a, b):
	    n=len(array)
	    i=0
	    j=n-1
	    
	    idx =0
	    
	    while idx<n:
	        if j<idx:
	            break
	        if array[idx]<a:
	            array[idx],array[i]=array[i],array[idx]
	            i+=1
	            idx+=1
	        elif array[idx]>b:
	           array[idx],array[j]=array[j],array[idx]
	           j-=1
	        else:
	           idx+=1
