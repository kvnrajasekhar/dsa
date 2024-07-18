//Link: https://www.geeksforgeeks.org/problems/missing-number-in-array1416/
class Solution {

    // Note that the size of the array is n-1
    int missingNumber(int n, int arr[]) {
        int res = 0;
        int sum = (n*(n+1))/2;
        for(int i = 0;i<n-1;i++){
            res += arr[i];
    }
    return sum-res;
    }
}
