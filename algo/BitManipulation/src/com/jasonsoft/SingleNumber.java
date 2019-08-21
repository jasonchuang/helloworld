package com.jasonsoft;

public class SingleNumber {

    /*
        Given a non-empty array of integers, every element appears twice except for one.
        Find that single one.

     */

    int singleNumber(int[] nums) {
        int ret = 0;
        for (int num : nums) {
            ret ^= num;
        }
        return ret;
    }
}
