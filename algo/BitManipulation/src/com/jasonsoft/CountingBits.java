package com.jasonsoft;

public class CountingBits {

    int hammingDistance(int n) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & (1 << i)) != 0) {
                count++;
            }
        }
        return count;
    }

    public int[] countingBits(int num) {
        int[] results = new int[num + 1];
        for (int i = 0; i <= num; i++) {
            results[i] = hammingDistance(i);
        }
        return results;
    }
}
