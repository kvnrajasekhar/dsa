#Link : https://www.naukri.com/code360/problems/maximize-sum_1376445
# Naukari code 360

from os import *
from sys import *
from collections import *
from math import *


def calculateMaximisedSum(arr1, arr2, N):

    # Write your code here
    # The function returns an integer denoting the maximised sum possible using the given algorithm for calculating the sum in the problem
    n=len(arr1)
    l=[[0,0] for _ in range(n)]
    l[0][0]=abs(arr1[0]-arr2[0])
    l[0][1]=abs(arr1[0]-arr2[0])
    for i in range(1,n):
        l[i][0]=abs(arr1[i]-arr2[i])+max(l[i-1][0]+abs(arr1[i]-arr2[i-1]),l[i-1][1]+abs(arr1[i]-arr1[i-1]))
        l[i][1]=abs(arr1[i]-arr2[i])+max(l[i-1][0]+abs(arr2[i]-arr2[i-1]),l[i-1][1]+abs(arr2[i]-arr1[i-1]))
    return max(l[n-1][0],l[n-1][1])
