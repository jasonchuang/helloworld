package com.jasonsoft;

public class ReverseBits {

    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        System.out.println(Integer.toBinaryString(n));
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result <<= 1;
            result |= n & 1;
            n >>>= 1;
        }

        // reverse integer
        // while (xxx)
        // if abs(x) * 10 > Integer.MAX, then abort
        // result = result * 10 + xxxx
        // x /= 10;

        return result;
    }
}
