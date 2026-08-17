# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The arrays are 0-indexed and the median is the middle value in the sorted merged array. If the length of the merged array is even, the median is the average of the two middle values. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the merged array is `[1, 2, 3]` and the median is `2`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the merged array is `[1, 2, 3, 4]` and the median is `(2 + 3)/2 = 2.5`.

## Approach
The algorithm uses binary search to find the partition point for both arrays, ensuring the elements on the left side of the partition point in both arrays are less than the elements on the right side. The median is then calculated based on the elements at the partition points. The binary search reduces the time complexity to O(log(min(m,n))).

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
                // If the total length is even
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
        
        // If no median is found
        return 0.0;
    }
};
```

## Test Cases
```
Input: nums1 = [1, 3], nums2 = [2]
Output: 2
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
```

## Key Takeaways
- The algorithm uses binary search to achieve a time complexity of O(log(min(m,n))).
- The partition points are adjusted based on the comparison of the elements at the partition points.
- The median is calculated based on whether the total length of the merged array is even or odd.