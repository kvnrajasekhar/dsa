#Link:https://www.geeksforgeeks.org/problems/two-swaps--155623/1


class Solution:
    def checkSorted(self, arr):
        #code here
        i=0
        count = 0
        while(i<len(arr)):
            if(arr[i] != i+1):
                firstindex = arr[i]-1 #since the numbers are natural and in series
                firstelement = arr[i]
                arr[i] = arr[firstindex]
                arr[firstindex] = firstelement
                count += 1
                i = i - 1
            i+=1    
        if(count==2 or count==0):
            return True
        else: return False
          
