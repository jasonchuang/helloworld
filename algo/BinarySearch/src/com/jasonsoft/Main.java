package com.jasonsoft;

public class Main {

    public static void main(String[] args) {
	// write your code here
        FirstBadVersion firstBadVersion = new FirstBadVersion();
        int result = firstBadVersion.firstBadVersion(100);
        System.out.println("firstBadVersion:" + result);

        BinarySearch binarySearch = new BinarySearch();
        result = binarySearch.search(new int[] {-1, 0, 3, 5, 9, 12}, 2);
        System.out.println("BinarySearch:" + result);


        TwoSumII twoSumII = new TwoSumII();
        int[] pair = twoSumII.twoSum(new int[] {2, 7, 11, 15}, 55);
        for (int n : pair) {
            System.out.println("TwoSumII index:" + n);
        }


        SearchInsertPosition searchInsertPosition = new SearchInsertPosition();
        result = searchInsertPosition.searchInsert(new int[] {1, 3, 5, 5, 5, 5, 5, 5, 6}, 5);
        System.out.println("SearchInsertPosition:" + result);
        result = searchInsertPosition.searchInsert(new int[] {1, 3, 5, 6}, 6);
        System.out.println("SearchInsertPosition:" + result);
        result = searchInsertPosition.searchInsert(new int[] {1, 3, 5, 6}, 7);
        System.out.println("SearchInsertPosition:" + result);


        FindTheDuplicateNumber findTheDuplicateNumber = new FindTheDuplicateNumber();
        result = findTheDuplicateNumber.findDuplicate(new int[] {3, 1, 3, 4, 2, 2});
        System.out.println("FindTheDuplicateNumber:" + result);

        FindFirstAndLastPositionOfElementInSortedArray findFirstLast = new FindFirstAndLastPositionOfElementInSortedArray();
        int[] results = findFirstLast.searchRange(new int[] {5, 7, 7, 8, 8, 10}, 7);
        System.out.println("findFirstLast:" + results[0] + ", and " + results[1]);
        results = findFirstLast.searchRange(new int[] {5, 7, 7, 8, 8, 10}, 6);
        System.out.println("findFirstLast:" + results[0] + ", and " + results[1]);
    }
}
