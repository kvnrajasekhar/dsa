// link : https://leetcode.com/problems/next-permutation/
class Solution {
        public static void reverseArray(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    public void nextPermutation(int[] nums) {
        int length = nums.length;
        int i, ind = -1;

        for (i = length - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                ind = i;
                break;
            }
        }

        if (ind == -1) {
            reverseArray(nums, 0, length - 1);
        } else {
            for (i = length - 1; i > ind; i--) {
                if (nums[i] > nums[ind]) {
                    int temp = nums[i];
                    nums[i] = nums[ind];
                    nums[ind] = temp;
                    break;
                }
            }
            reverseArray(nums, ind + 1, length - 1);
        }
    }
        
    }
