# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the combined array. The median is the middle value in the sorted array. If the total number of elements is odd, the median is the middle element. If the total number of elements is even, the median is the average of the two middle elements. The input arrays are sorted in ascending order.

## Approach
The algorithm involves merging the two sorted arrays into one and then finding the median. Since the input arrays are sorted, we can use a two-pointer technique to merge them efficiently. We then find the median based on whether the total number of elements is odd or even.

## Complexity
- Time: O(m + n)
- Space: O(m + n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Merge the two sorted arrays into one
        vector<int> merged;
        int i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1[i] < nums2[j]) {
                merged.push_back(nums1[i]);
                i++;
            } else {
                merged.push_back(nums2[j]);
                j++;
            }
        }
        // Add remaining elements from nums1
        while (i < nums1.size()) {
            merged.push_back(nums1[i]);
            i++;
        }
        // Add remaining elements from nums2
        while (j < nums2.size()) {
            merged.push_back(nums2[j]);
            j++;
        }
        // Find the median
        int n = merged.size();
        if (n % 2 == 0) {
            // If the total number of elements is even, return the average of the two middle elements
            return (merged[n / 2 - 1] + merged[n / 2]) / 2.0;
        } else {
            // If the total number of elements is odd, return the middle element
            return merged[n / 2];
        }
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
- The two-pointer technique can be used to merge two sorted arrays efficiently.
- The median of a sorted array can be found in constant time if the array is already sorted.
- When dealing with floating-point numbers, it's often necessary to use a specific data type (e.g., `double`) to avoid integer division.