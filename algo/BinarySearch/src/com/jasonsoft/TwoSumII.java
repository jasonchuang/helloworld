package com.jasonsoft;

public class TwoSumII {

    public int[] twoSum(int[] numbers, int target) {
        int L = 0, R = numbers.length - 1;
        while (L < R) {
            if (numbers[L] + numbers[R] == target) {
                return new int[] {L, R};
            } else if (numbers[L] + numbers[R] < target) {
                L++;
            } else {
                R--;
            }
        }

        return new int[] {-1, -1};
    }
}
