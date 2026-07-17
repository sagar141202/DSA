# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the combined array. The median is the middle value in the sorted array. If the total number of elements is odd, the median is the middle element. If the total number of elements is even, the median is the average of the two middle elements. The input arrays are sorted in ascending order.

## Approach
The algorithm merges the two sorted arrays into one sorted array, then calculates the median based on whether the total length is odd or even. The merging can be done using a two-pointer technique to achieve a time complexity of O(m + n).

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
        // Merge two sorted arrays into one sorted array
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
        // Append the remaining elements
        while (i < nums1.size()) {
            merged.push_back(nums1[i]);
            i++;
        }
        while (j < nums2.size()) {
            merged.push_back(nums2[j]);
            j++;
        }
        
        int n = merged.size();
        // Calculate the median
        if (n % 2 == 0) {
            return (merged[n / 2 - 1] + merged[n / 2]) / 2.0;
        } else {
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
- The median of a sorted array can be calculated based on whether the length of the array is odd or even.
- The time complexity of merging two sorted arrays is O(m + n), where m and n are the lengths of the input arrays.