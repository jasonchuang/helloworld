package com.jasonsoft;

public class Main {

    public static void main(String[] args) {
        NumberOf1Bits numberOf1Bits = new NumberOf1Bits();
        int result = numberOf1Bits.hammingWeight(-1);
        System.out.println(result);

        HammingDistance hammingDistance = new HammingDistance();
        result = hammingDistance.hammingDistance(1, 4);
        System.out.println(result);

        SingleNumber singleNumber = new SingleNumber();
        result = singleNumber.singleNumber(new int[] {1, 1, 2, 3, 3, 4, 2} );
        System.out.println(result);

        PowerOfTwo powerOfTwo = new PowerOfTwo();
        System.out.println(powerOfTwo.isPowerOfTwo(16));

        CountingBits countingBits = new CountingBits();
        for (int n : countingBits.countingBits(5)) {
            System.out.println(n);
        }

        ReverseBits reverseBits = new ReverseBits();
        long test = 4294967293L;
        System.out.println(Integer.toBinaryString(reverseBits.reverseBits((int) test)));
    }
}
