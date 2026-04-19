# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The arrays are 0-indexed. If the total number of elements is odd, the median is the middle element. If the total number of elements is even, the median is the average of the two middle elements. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `2`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3)/2 = 2.5`.

## Approach
The algorithm uses binary search to find the median of two sorted arrays. It maintains two pointers, one for each array, and adjusts them based on the comparison of the current elements. The algorithm continues until the pointers reach the middle of the combined array. The median is then calculated based on the elements at the middle indices.

## Complexity
- Time: O(log(min(m,n)))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Make sure nums1 is the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int x = nums1.size();
        int y = nums2.size();
        int start = 0;
        int end = x;

        while (start <= end) {
            int partitionX = (start + end) / 2;
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
                end = partitionX - 1;
            } else {
                start = partitionX + 1;
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
- The algorithm uses binary search to reduce the time complexity to O(log(min(m,n))).
- The pointers are adjusted based on the comparison of the current elements to ensure the median is found correctly.
- The solution handles both even and odd total lengths of the combined array.