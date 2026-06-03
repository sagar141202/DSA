# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the combined array. The median is the middle value in the sorted array. If the total number of elements is odd, the median is the middle element. If the total number of elements is even, the median is the average of the two middle elements. The input arrays are non-empty and the length of `nums1` and `nums2` will not exceed 2 * 10^4. The arrays may contain duplicate elements.

## Approach
The algorithm uses binary search to find the median of the combined array. We calculate the total length of the combined array and then use binary search to find the partition point for both arrays. The partition point is the point where the elements on the left side of the partition point in both arrays are less than or equal to the elements on the right side.

## Complexity
- Time: O(log(min(m, n)))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Make sure that nums1 is the smaller array to simplify the code
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int x = nums1.size();
        int y = nums2.size();
        int low = 0;
        int high = x;

        while (low <= high) {
            // Partition point for nums1
            int partitionX = (low + high) / 2;
            // Partition point for nums2
            int partitionY = (x + y + 1) / 2 - partitionX;

            // Values at the partition points
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];

            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];

            // Check if the partition is correct
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // If the total length is odd, return the max of the left partition
                if ((x + y) % 2 == 0) {
                    return (double)(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2;
                } else {
                    return (double)max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                // If the max of the left partition in nums1 is greater than the min of the right partition in nums2,
                // move the partition point to the left in nums1
                high = partitionX - 1;
            } else {
                // If the max of the left partition in nums1 is less than the min of the right partition in nums2,
                // move the partition point to the right in nums1
                low = partitionX + 1;
            }
        }
    }
};
```

## Test Cases
```
Input: nums1 = [1, 3], nums2 = [2]
Output: 2.0
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
```

## Key Takeaways
- The algorithm uses binary search to find the median of the combined array, which reduces the time complexity to O(log(min(m, n))).
- The partition point is used to divide the combined array into two parts, and the values at the partition points are used to determine if the partition is correct.
- The algorithm handles both odd and even length combined arrays and returns the median accordingly.