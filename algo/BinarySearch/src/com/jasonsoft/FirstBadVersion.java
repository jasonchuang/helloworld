package com.jasonsoft;

public class FirstBadVersion {

    /*
    developed based on the previous version, all the versions after a bad version are also bad.
    Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
    which causes all the following ones to be bad.
     */
    static boolean isBadVersion(int version) {
        if (version >= 22) {
            return true;
        }
        return false;
    }

    public int firstBadVersion(int n) {
        System.out.println("FirstBadVersion");
        /*
        for (int i = 1; i <= n; i++) {
            if (isBadVersion(i)) {
                return i;
            }
        }
        */
        int L = 1, R = n;
        while (L < R) {
            int M = (L + R) / 2;
            System.out.println("L:" + L + ", R:" + R);
            if (isBadVersion(M)) {
                R = M;
                System.out.println("isBadVersion:");
            } else {
                L = M + 1;
                System.out.println("Not isBadVersion:");
            }
        }

        return L;
    }
}
