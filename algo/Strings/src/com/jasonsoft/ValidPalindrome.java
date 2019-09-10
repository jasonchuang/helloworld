package com.jasonsoft;

public class ValidPalindrome {

    public boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            // avoid i IOOB, and reach the same pos with j
            // let i and j both are in the valid range for charAt
            // hence the below equals case can return true
            while (i < j && !Character.isLetterOrDigit(s.charAt(j))) {
                System.out.println("j is:" + i);
                j--;
            }

            while (i < j && !Character.isLetterOrDigit(s.charAt(i))) {
                System.out.println("i is:" + i);
                i++;
            }

            System.out.println("compare i and j:" + i + ", j:" + j);
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }

            i++;
            j--;
        }
        return true;
    }
}
