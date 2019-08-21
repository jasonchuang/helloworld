package com.jasonsoft;

public class Main {

    public static void main(String[] args) {
        NumberOf1Bits numberOf1Bits = new NumberOf1Bits();
        int result = numberOf1Bits.numberOf1Bits(256);
        System.out.println(result);
        result = numberOf1Bits.numberOf1Bits2(26);
        System.out.println(result);

        result = numberOf1Bits.hammingDistance(1, 4);
        System.out.println(result);
    }
}
