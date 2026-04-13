# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays, `nums1` and `nums2`, find the median of the combined array. The total number of elements in both arrays is `m + n`, where `m` and `n` are the lengths of `nums1` and `nums2`, respectively. If the total number of elements is odd, the median is the middle element. If the total number of elements is even, the median is the average of the two middle elements. The input arrays are non-empty and contain only integers.

## Approach
The algorithm merges the two sorted arrays and then finds the median based on whether the total length is odd or even. This can be achieved by using a two-pointer technique to merge the arrays. The time complexity is reduced by considering the smaller array to determine the partition point.

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
        
        return 0.0;
    }
};
```

## Test Cases
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
```

## Key Takeaways
- The algorithm uses a binary search approach to find the partition point in the smaller array.
- It ensures that the elements on the left side of the partition point in both arrays are less than or equal to the elements on the right side.
- The time complexity is reduced to O(log(min(m, n))) by using a binary search approach.