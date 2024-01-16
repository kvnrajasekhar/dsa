// link : https://leetcode.com/problems/maximum-subarray/
//time complexity : O(n)

class Solution {
    public int maxSubArray(int[] nums) {
        int l=nums.length;
        if(l==1)
        return nums[0];
        int maxi=nums[0];
    //    int i=0;
    //     while(i<l){
    //         int j=i;
    //         int sum=0;
    //         while(j<l){
    //             sum=sum+nums[j];
    //             if(sum>maxi){
    //                 maxi=sum;
    //             }
    //             j=j+1;
    //         }
    //         i=i+1;
    //     }
    //     return maxi;
    int sum = nums[0];
        for (int i = 1; i < l; i++) {
            sum = Math.max(nums[i], sum + nums[i]);
          maxi = Math.max(maxi, sum);
        }
        return maxi;
     }
}
