# Median of Two Sorted Arrays

## Problem Statement
Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, find the median of the combined array. The median is the middle value in the sorted array. If the total number of elements is even, the median is the average of the two middle values. The input arrays are 0-indexed and contain only integers. The length of `nums1` and `nums2` will not exceed 10^4.

## Approach
The algorithm merges the two sorted arrays into a single array and then finds the median. If the total length is odd, the median is the middle element. If the total length is even, the median is the average of the two middle elements. The merging can be done using a simple iterative approach or by utilizing a data structure like a priority queue.

## Complexity
- Time: O((m + n) log(m + n))
- Space: O(m + n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Merge the two sorted arrays into a single array
        vector<int> merged;
        merged.reserve(nums1.size() + nums2.size());
        merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), back_inserter(merged));
        
        int n = merged.size();
        // If the total length is odd, the median is the middle element
        if (n % 2 == 1) {
            return merged[n / 2];
        }
        // If the total length is even, the median is the average of the two middle elements
        else {
            return (merged[n / 2 - 1] + merged[n / 2]) / 2.0;
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
- Merging two sorted arrays can be done using the `merge` function from the C++ Standard Template Library (STL).
- The median of a sorted array can be found by checking if the length is odd or even and returning the corresponding middle value(s).
- Using a `vector` to store the merged array allows for dynamic resizing and efficient insertion of elements.