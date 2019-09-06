package com.jasonsoft;

public class SearchInsertPosition {

    public int searchInsert(int[] nums, int target) {
        int L = 0, R = nums.length - 1;
        while (L < R) {
            System.out.println("L:" + L + ", R:" + R);
            int M = (L + R) / 2;
            /*
            new int[] {1, 3, 5, 6}, 10);
            0, 3
            1, 3
            2, 3
            3, 3 (break)
            */
            if (nums[M] < target) {
                L = M + 1;
            } else {
                R = M;
            }

             /*
            new int[] {1, 3, 5, 6}, 0);
            0, 3
            0, 1
            0, 0 (break)
             */



            /*
             0, 3
             1, 3
             2, 3
             2, 3
             2, 3
             (L 被卡住, 剩兩個的時候 ＧＧ)
             */

          /*  if (nums[M] > target) {
                R = M - 1;
            } else {
                L = M;
            }

           */
        }
        return nums[L] < target ? L + 1 : L;
    }
}
