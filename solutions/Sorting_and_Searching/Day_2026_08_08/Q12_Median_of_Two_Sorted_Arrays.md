# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the combined array. The median is the middle value in an ordered integer list. If the total number of elements is even, the median is the mean of the two middle numbers. The input arrays are non-empty and the total number of elements will not exceed 2000. For example, given `nums1 = [1, 3]` and `nums2 = [2]`, the median is `2`. Given `nums1 = [1, 2]` and `nums2 = [3, 4]`, the median is `(2 + 3)/2 = 2.5`.

## Approach
We can solve this problem by merging the two sorted arrays into one and then finding the median. The algorithm involves comparing elements from both arrays and placing the smaller one into the merged array. We can then calculate the median based on the length of the merged array.

## Complexity
- Time: O(log(min(m, n)))
- Space: O(log(min(m, n)))

## C++ Solution
```cpp
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        
        // Ensure that nums1 is the smaller array
        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int low = 0;
        int high = m;
        
        while (low <= high) {
            int partitionX = (low + high) / 2;
            int partitionY = (m + n + 1) / 2 - partitionX;
            
            int maxLeftX = (partitionX == 0) ? INT_MIN : nums1[partitionX - 1];
            int minRightX = (partitionX == m) ? INT_MAX : nums1[partitionX];
            
            int maxLeftY = (partitionY == 0) ? INT_MIN : nums2[partitionY - 1];
            int minRightY = (partitionY == n) ? INT_MAX : nums2[partitionY];
            
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                if ((m + n) % 2 == 0) {
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
Input: nums1 = [1, 3], nums2 = [2]
Output: 2
Input: nums1 = [1, 2], nums2 = [3, 4]
Output: 2.5
```

## Key Takeaways
- The problem can be solved using a binary search approach to find the partition point for the two arrays.
- The time complexity can be reduced to O(log(min(m, n))) by using binary search.
- The space complexity is O(log(min(m, n))) due to the recursive call stack.