package com.jasonsoft;

public class FindFirstAndLastPositionOfElementInSortedArray {

    // 2, 3, 5, 5, 5, 6, 7
    int getFirstPosition(int[] nums, int target) {
        int L = 0, R = nums.length - 1;
        while (L < R) {
            int M = (L + R) / 2;
            // strict greater rule for L forwarding,
            // easy to left forwarding
            if (nums[M] < target) {
                L = M + 1;
            } else {
                // equals case hint forwarding LEFT side
                R = M;
            }
        }
        return nums[L] == target ? L : -1;
    }

  /*  if (nums[M] <= target) {
        L = M;
    } else {
        R = M - 1;
    }
    */


    /*
    However, if you want the index of the rightmost element that is equal to val
    then you need to change the < operator to > and mid should be given by
    mid = (left+right+1)/2;
 */

    int getLastPosition(int[] nums, int target) {
        int L = 0, R = nums.length - 1;
        while (L < R) {
            int M = (L + R + 1) / 2;
            System.out.println("L:" + L + ", R:" + R + ", M:" + M);

            if (nums[M] > target) {
                R = M - 1;
            } else {
                // equals case hint forwarding RIGHT side
                // it depends on M assigned to whom!!!!
                L = M;
            }
        }
        return nums[L] == target ? L : -1;
    }

    // key point is the equals handling
    //  {5, 7, 7, 8, 8, 10}, 8);
    //     // 2, 3, 5, 5, 5, 6, 7
    int getLastPosition2(int[] nums, int target) {
        int L = 0, R = nums.length;
        while (L < R) {
            int M = (L + R + 1) / 2;
            System.out.println("L:" + L + ", R:" + R + ", M:" + M);
            if (nums[M] <= target) {
                L = M;
            } else {
                R = M - 1;
            }
        }
        return nums[L] == target ? L : -1;
    }


    public int[] searchRange(int[] nums, int target) {
        int[] input0 = new int[] {2, 3, 10, 2, 4, 8, 1} ;
        int[] input1 = new int[] {7, 9, 5, 6, 3, 2} ;
        int maxDiff = 0;
        int min = Integer.MAX_VALUE, min_index = -1;
        int max = Integer.MIN_VALUE, max_index = -1;
        for (int i = 0; i < input0.length; i++) {
            if (input0[i] > max && i > max_index) {
                max = input0[i];
                maxDiff = Math.max(maxDiff, max - min);
            }
            if (input0[i] < min && i > min_index) {
                min = input0[i];
            }
            System.out.println("max:" + max + ", min:" + min + ", maxDiff:" + maxDiff);
        }

        return new int[] {getFirstPosition(nums, target),
                getLastPosition(nums, target)};
    }
}
