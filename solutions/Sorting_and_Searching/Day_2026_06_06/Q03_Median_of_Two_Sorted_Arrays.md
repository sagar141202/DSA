# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the combined array. The median is the middle value in the sorted combined array. If the total number of elements is even, the median is the average of the two middle values. The input arrays are non-empty and the total number of elements will not exceed 2 * 10^5. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `2.0`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3) / 2 = 2.5`.

## Approach
We can use a binary search approach to find the median of the combined array. The idea is to partition both arrays such that the elements on the left side of the partition are less than or equal to the elements on the right side. We can then use the partition to calculate the median.

## Complexity
- Time: O(log(min(m, n)))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // make sure that nums1 is the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int x = nums1.size();
        int y = nums2.size();
        
        int low = 0;
        int high = x;
        
        while (low <= high) {
            int partitionX = (low + high) / 2;
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
                high = partitionX - 1;
            } else {
                low = partitionX + 1;
            }
        }
        
        // if we reach here, it means that the input arrays are not sorted
        throw runtime_error("Input arrays are not sorted");
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
- The binary search approach is used to find the median of the combined array.
- The time complexity is O(log(min(m, n))) where m and n are the sizes of the input arrays.
- The space complexity is O(1) as we only use a constant amount of space to store the variables.