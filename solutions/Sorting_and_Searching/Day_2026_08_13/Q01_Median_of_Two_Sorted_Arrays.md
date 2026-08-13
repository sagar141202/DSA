# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The median of a single array is the middle element when the array is sorted in ascending order. If the array has an even number of elements, the median is the average of the two middle elements. For example, given `nums1 = [1,3]` and `nums2 = [2]`, the median is `2.0`. Given `nums1 = [1,2]` and `nums2 = [3,4]`, the median is `(2 + 3)/2 = 2.5`.

## Approach
The algorithm uses binary search to find the median of two sorted arrays. We try to partition both arrays such that elements on the left side of the partition are less than or equal to elements on the right side. The partition is adjusted based on the comparison of elements at the partition boundary. The process is repeated until the correct partition is found.

## Complexity
- Time: O(log(min(m,n)))
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Make sure that nums1 is the smaller array to simplify the logic
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
            
            // Calculate the values at the partition boundaries
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
            } else if (maxLeftX > minRightY) {
                // If the partition is too far to the right, move it to the left
                high = partitionX - 1;
            } else {
                // If the partition is too far to the left, move it to the right
                low = partitionX + 1;
            }
        }
        
        // If the function hasn't returned by now, something is wrong
        throw runtime_error("Failed to find median");
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
- The algorithm uses binary search to find the median of two sorted arrays in O(log(min(m,n))) time complexity.
- The key to the algorithm is to partition both arrays such that elements on the left side of the partition are less than or equal to elements on the right side.
- The partition is adjusted based on the comparison of elements at the partition boundary until the correct partition is found.