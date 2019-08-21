package com.jasonsoft;

public class PowerOfTwo {

    public boolean isPowerOfTwo(int n) {
        return (n & n-1) == 0;
    }
}
