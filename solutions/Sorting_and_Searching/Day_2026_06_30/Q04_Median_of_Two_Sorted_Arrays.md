# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The arrays are 0-indexed, and the median of an array with an even number of elements is the average of the two middle elements. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `(1 + 2) / 2 = 1.5`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3) / 2 = 2.5`.

## Approach
The algorithm uses binary search to find the partition point for both arrays, ensuring that elements on the left side of the partition point in both arrays are less than or equal to elements on the right side. This approach allows for an efficient calculation of the median. The intuition is to balance the two arrays such that the elements on the left side of the partition in both arrays are less than or equal to the elements on the right side.

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
        // Make sure that nums1 is the smaller array to simplify the logic
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int x = nums1.size();
        int y = nums2.size();
        
        // Initialize the low and high pointers for binary search
        int low = 0;
        int high = x;
        
        while (low <= high) {
            // Partition point for nums1
            int partitionX = (low + high) / 2;
            // Partition point for nums2 such that the total elements on the left side are (x + y + 1) / 2
            int partitionY = ((x + y + 1) / 2) - partitionX;
            
            // Calculate the values at the partition points
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];
            
            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];
            
            // Check if the partition is correct
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // If the total number of elements is odd, return the max of the left side
                if ((x + y) % 2 == 0) {
                    return (double)(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2;
                } else {
                    return (double)max(maxLeftX, maxLeftY);
                }
            } 
            // If the partition is not correct, adjust the pointers accordingly
            else if (maxLeftX > minRightY) {
                high = partitionX - 1;
            } else {
                low = partitionX + 1;
            }
        }
        
        // If no median is found, return -1 (this should not happen)
        return -1;
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
- The algorithm uses binary search to efficiently find the median of two sorted arrays.
- The partition point is crucial in determining the median, and it must be adjusted based on the comparison of elements at the partition points.
- The solution handles both odd and even total number of elements and returns the correct median.