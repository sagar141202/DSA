# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The median is the middle value in the sorted array. If the total number of elements is even, the median is the average of the two middle values. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `2.0`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3)/2 = 2.5`.

## Approach
The algorithm uses binary search to find the partition point for both arrays, ensuring that elements on the left side of the partition point in both arrays are less than or equal to elements on the right side. This approach allows us to find the median in logarithmic time complexity. We calculate the total length of both arrays and determine if it's odd or even to decide how to calculate the median.

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
        // Ensure that nums1 is the smaller array to simplify the logic
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
            // Partition point for nums2 such that elements on the left side of both partitions are equal
            int partitionY = (x + y + 1) / 2 - partitionX;
            
            // Values at the partition points
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];
            
            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];
            
            // Check if the partition is correct
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // If the total length is odd, return the max of the left side
                if ((x + y) % 2 == 0) {
                    return (double)(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2;
                } else {
                    return (double)max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                // If maxLeftX is greater than minRightY, move the partition to the left
                high = partitionX - 1;
            } else {
                // If maxLeftX is less than minRightY, move the partition to the right
                low = partitionX + 1;
            }
        }
        
        // If no median is found, return an error or a default value
        return 0.0;
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
- The key to solving this problem efficiently is using binary search to find the partition point.
- Ensuring that `nums1` is the smaller array simplifies the logic and reduces the number of edge cases to consider.
- The median calculation depends on whether the total length of the two arrays is odd or even.