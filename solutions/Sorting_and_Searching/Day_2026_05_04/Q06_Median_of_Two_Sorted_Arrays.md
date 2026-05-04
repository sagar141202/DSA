# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the two sorted arrays. The overall run time complexity should be O(log(min(m,n))). The arrays are 0-indexed and the median of an array with an odd length is the middle element, while the median of an array with an even length is the average of the two middle elements. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `2.0`, and given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3)/2 = 2.5`.

## Approach
The algorithm uses binary search to find the partition point for both arrays, ensuring that elements on the left side of the partition point in both arrays are less than or equal to elements on the right side. This approach allows us to find the median in logarithmic time complexity. We maintain a balance between the two arrays by adjusting the partition points. The key insight is to ensure that the total number of elements on the left side of the partition is equal to the total number of elements on the right side when the total number of elements is even.

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
            // Partition point for nums2
            int partitionY = (x + y + 1) / 2 - partitionX;
            
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
            } else if (maxLeftX > minRightY) {
                // If the max of the left side of nums1 is greater than the min of the right side of nums2,
                // move the partition point to the left in nums1
                high = partitionX - 1;
            } else {
                // If the max of the left side of nums2 is greater than the min of the right side of nums1,
                // move the partition point to the right in nums1
                low = partitionX + 1;
            }
        }
        
        // This should not happen
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
- The key to solving this problem efficiently is to use binary search to find the partition point.
- Ensuring that `nums1` is the smaller array simplifies the logic and reduces the number of edge cases to consider.
- The time complexity of O(log(min(m,n))) makes this solution efficient for large inputs.