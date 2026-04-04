# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the combined array. The median is the middle value in an ordered integer list. If the total number of elements is even, the median is the average of the two middle values. Assume that `0 <= m <= 100` and `0 <= n <= 100`, and the total number of elements is between `0` and `200`.

## Approach
The approach is to merge the two sorted arrays and then find the median. Since the arrays are already sorted, we can use a two-pointer technique to merge them in linear time. After merging, we can find the median by checking if the total length is odd or even.

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
        // Merge the two sorted arrays
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
        // Add any remaining elements
        while (i < nums1.size()) {
            merged.push_back(nums1[i]);
            i++;
        }
        while (j < nums2.size()) {
            merged.push_back(nums2[j]);
            j++;
        }
        // Find the median
        int n = merged.size();
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
- The time complexity is O(m + n) because we are merging the two arrays in linear time.
- The space complexity is O(m + n) because we are storing the merged array.
- We use a two-pointer technique to merge the two sorted arrays.