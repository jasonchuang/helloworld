package com.jasonsoft;

public class NumberOf1Bits {

    /*
        Write a function that takes an unsigned integer and return the number of '1' bits it has
        (also known as the Hamming weight).

        Input: 00000000000000000000000000001011
        Output: 3
        Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
     */

    int hammingWeight(int n) {
        int count = 0;

        System.out.println("n is:" + n);
        int mask = 1;
        for (int i = 0; i < 32; i++) {
          //  System.out.println(n & (1 << i));
            System.out.println("mask is:" + mask);
            if ((n & (1 << i)) != 0) {
                count++;
            }
            mask <<= 1;
        }
        return count;
    }


    int hammingWeight2(int n) {
        int count = 0;
        while (n != 0) {
            count++;
            n &= n - 1;
        }
        return count;
    }

    // OR keep n = n & n-1
    // somebody shifts then exe AND
    int getBit(int n, int k) {
        return (n >> k) & 1;
    }

    // setBit => n | (1 << k)
    // clearBit => n & ~(1 << k)

    int hammingDistance(int x, int y) {
        /*
        int count = 0;
        System.out.println("x is:" + x + ", y is:" + y);
        for (int i = 0; i < 32; i++) {
            //  System.out.println(n & (1 << i));
            System.out.println("x's bit is:" + (x >> i) + ", y is:" + (y >> i));
            if ((getBit(x, i) ^ getBit(y, i)) == 1) {
                count++;
            }
        }
        */
        return hammingWeight(x ^ y);
    }
}
