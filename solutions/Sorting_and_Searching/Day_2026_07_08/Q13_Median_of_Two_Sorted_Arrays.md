# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The median is the middle value in the sorted array. If the total number of elements is even, the median is the average of the two middle values. The input arrays are sorted in non-decreasing order, and the total number of elements will not exceed 2000. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `2.0`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3) / 2 = 2.5`.

## Approach
The algorithm uses binary search to find the median of two sorted arrays. It calculates the total length of both arrays and determines the half length. Then, it performs a binary search on the smaller array to find the partition point that divides the combined array into two halves with equal sums. The median is then calculated based on the values at the partition points.

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
        // Ensure that nums1 is the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int x = nums1.size();
        int y = nums2.size();
        int low = 0;
        int high = x;

        while (low <= high) {
            int partitionX = (low + high) / 2;
            int partitionY = (x + y + 1) / 2 - partitionX;

            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];

            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                if ((x + y) % 2 == 0) {
                    return (double)(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2;
                } else {
                    return (double)max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                high = partitionX - 1;
            } else {
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
- The algorithm uses binary search to find the median of two sorted arrays in O(log(min(m, n))) time complexity.
- The space complexity is O(1) as it only uses a constant amount of space.
- The algorithm ensures that the smaller array is always `nums1` to simplify the logic and reduce the number of edge cases.