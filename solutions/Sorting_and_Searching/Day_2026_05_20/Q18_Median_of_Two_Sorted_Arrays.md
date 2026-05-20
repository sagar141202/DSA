# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The median of a single number is the number itself, and the median of two numbers is the average of the two numbers. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `2.0`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3)/2 = 2.5`.

## Approach
To find the median of two sorted arrays, we can use binary search to achieve a time complexity of O(log(min(m,n))). The idea is to partition both arrays such that the elements on the left side of the partition are less than the elements on the right side. We can then adjust the partition to find the median.

## Complexity
- Time: O(log(min(m,n)))
- Space: O(1)

## C++ Solution
```cpp
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
            int partitionY = ((x + y + 1) / 2) - partitionX;
            
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
        
        // Should not reach here
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
- The key to solving this problem is to use binary search to find the partition that divides the two arrays into two halves with the same total number of elements.
- We need to consider the case where the total number of elements is odd or even to calculate the median correctly.
- The time complexity of the solution is O(log(min(m,n))), which is more efficient than a simple merge and sort approach.