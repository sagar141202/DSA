# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the combined array. The median is the middle value in the sorted array. If the total number of elements is even, the median is the average of the two middle values. The input arrays are non-empty and the length of `nums1` and `nums2` will not exceed 2000. The elements of `nums1` and `nums2` are all integers. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `2`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3)/2 = 2.5`.

## Approach
The algorithm uses binary search to find the median of the combined array. We try to partition the two arrays such that the elements on the left side of the partition are less than or equal to the elements on the right side. The partition is done in a way that the total number of elements on the left side is equal to the total number of elements on the right side if the total number of elements is even.

## Complexity
- Time: O(log(min(m, n)))
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Make sure that nums1 is the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int x = nums1.size();
        int y = nums2.size();
        
        int low = 0;
        int high = x;
        
        while (low <= high) {
            // Partition the arrays
            int partitionX = (low + high) / 2;
            int partitionY = (x + y + 1) / 2 - partitionX;
            
            // Calculate the values at the partition
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? INT_MAX : nums1[partitionX];
            
            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? INT_MAX : nums2[partitionY];
            
            // Check if the partition is correct
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // Calculate the median
                if ((x + y) % 2 == 0) {
                    return (double)(max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2;
                } else {
                    return (double)max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                // Move the partition to the left
                high = partitionX - 1;
            } else {
                // Move the partition to the right
                low = partitionX + 1;
            }
        }
        
        // If we reach this point, it means that the input arrays are not sorted
        throw invalid_argument("Input arrays are not sorted");
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
- The algorithm uses binary search to find the median of the combined array in O(log(min(m, n))) time.
- The space complexity is O(1) because we only use a constant amount of space to store the variables.
- The algorithm assumes that the input arrays are sorted, and it throws an exception if they are not.