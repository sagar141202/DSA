# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The arrays are 0-indexed and the median is the middle value in the sorted array. If the total number of elements is even, the median is the average of the two middle values. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `2`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3)/2 = 2.5`.

## Approach
We can use binary search to find the median of two sorted arrays. The idea is to partition both arrays into two parts each, such that the elements in the left part of both arrays are less than the elements in the right part. We can then adjust the partition based on the comparison of the elements at the partition boundary.

## Complexity
- Time: O(log(min(m,n)))
- Space: O(1)

## C++ Solution
```cpp
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
            // Partition for nums1
            int partitionX = (low + high) / 2;
            // Partition for nums2
            int partitionY = (x + y + 1) / 2 - partitionX;
            
            // Calculate the values at the partition boundary
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
                // If the partition is too far to the right, move it to the left
                high = partitionX - 1;
            } else {
                // If the partition is too far to the left, move it to the right
                low = partitionX + 1;
            }
        }
        
        // If no median is found, return -1
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
- The time complexity of the solution is O(log(min(m,n))), where m and n are the sizes of the two arrays.
- The space complexity of the solution is O(1), as no extra space is used.
- The solution uses binary search to find the median of the two sorted arrays.