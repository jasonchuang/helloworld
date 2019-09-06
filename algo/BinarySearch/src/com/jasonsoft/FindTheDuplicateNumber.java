package com.jasonsoft;

import java.util.HashSet;
import java.util.Set;

public class FindTheDuplicateNumber {

    public int findDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return num;
            }
            seen.add(num);
        }

        return -1;
    }
}