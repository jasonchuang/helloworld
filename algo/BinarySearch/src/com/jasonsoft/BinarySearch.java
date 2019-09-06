package com.jasonsoft;

public class BinarySearch {

    public int search(int[] nums, int target) {
        int L = 0, R = nums.length - 1;
        while (L <= R) {
            int M = (L + R) / 2;
            if (nums[M] == target) {
                return M;
            } else if (nums[M] < target) {
                L = M + 1;
            } else {
                R = M - 1;
            }
        }
        return -1;
    }
}
