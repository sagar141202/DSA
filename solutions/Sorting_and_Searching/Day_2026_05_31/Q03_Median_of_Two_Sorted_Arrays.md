# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The arrays are 0-indexed and can contain duplicate elements. If the total number of elements is odd, the median is the middle element. If the total number of elements is even, the median is the average of the two middle elements.

## Approach
The algorithm uses a binary search approach to find the median. It calculates the partition point for both arrays such that the elements on the left side of the partition point in both arrays are less than or equal to the elements on the right side. The partition point is adjusted based on the comparison of the elements at the partition point.

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
        // Make sure that nums1 is the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int x = nums1.size();
        int y = nums2.size();
        
        int start = 0;
        int end = x;
        
        while (start <= end) {
            // Partition point for nums1
            int partitionX = (start + end) / 2;
            // Partition point for nums2
            int partitionY = (x + y + 1) / 2 - partitionX;
            
            // Calculate the values at the partition points
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];
            
            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];
            
            // Check if the partition is correct
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // If the total number of elements is odd
                if ((x + y) % 2 == 0) {
                    return (double)(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2;
                } else {
                    return (double)max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                // If the partition point is too far to the right
                end = partitionX - 1;
            } else {
                // If the partition point is too far to the left
                start = partitionX + 1;
            }
        }
        
        // If no median is found
        return 0.0;
    }
};
```

## Test Cases
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5
```

## Key Takeaways
- The binary search approach is used to find the median in O(log(min(m,n))) time complexity.
- The partition point is adjusted based on the comparison of the elements at the partition point.
- The solution handles both odd and even total number of elements cases.