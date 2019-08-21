package com.jasonsoft;

public class HammingDistance {

    /*
        Write a function that takes an unsigned integer and return the number of '1' bits it has
        (also known as the Hamming weight).
     */

    int hammingDistance(int n) {
        int count = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & (1 << i)) != 0) {
                count++;
            }
        }
        return count;
    }

    int hammingDistance(int x, int y) {
        return hammingDistance(x ^ y);
    }
}
