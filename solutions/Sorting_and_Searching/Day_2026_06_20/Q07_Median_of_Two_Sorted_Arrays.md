# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The arrays are 0-indexed and the median is the middle value in the sorted array. If the total number of elements is even, the median is the average of the two middle values. For example, given `nums1 = [1,3]` and `nums2 = [2]`, the median is `2`. Given `nums1 = [1,2]` and `nums2 = [3,4]`, the median is `(2 + 3)/2 = 2.5`.

## Approach
The algorithm uses binary search to find the median of the two sorted arrays. It calculates the partition point for both arrays such that the elements on the left side of the partition point in both arrays are less than the elements on the right side. The partition point is adjusted based on the comparison of the elements at the partition point.

## Complexity
- Time: O(log(min(m,n)))
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
        
        // If we reach here, it means that the input arrays are not sorted
        throw runtime_error("Input arrays are not sorted");
    }
};
```

## Test Cases
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5
```

## Key Takeaways
- The algorithm uses binary search to find the median of the two sorted arrays, reducing the time complexity to O(log(min(m,n))).
- The partition point is adjusted based on the comparison of the elements at the partition point to ensure that the elements on the left side of the partition point are less than the elements on the right side.
- The algorithm handles both even and odd total number of elements and returns the correct median value.