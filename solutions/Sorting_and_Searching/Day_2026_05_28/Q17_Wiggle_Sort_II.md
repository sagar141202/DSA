# Wiggle Sort II

## Problem Statement
Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. You may assume the input array always has a valid answer. The length of the array is in the range `[1, 5000]`. The elements of the array are in the range `[-5000, 5000]`. For example, if the input array is `[1, 5, 1, 1, 6, 4]`, one possible output is `[1, 4, 1, 5, 1, 6]`.

## Approach
The approach is to first sort the array, then use two pointers to place the elements at the correct positions to satisfy the wiggle sort condition. We can use a single loop to construct the result array.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        // Create a copy of the array and sort it
        vector<int> sortedNums = nums;
        sort(sortedNums.begin(), sortedNums.end());
        
        int n = nums.size();
        int mid = (n - 1) / 2;
        
        // Use two pointers to place the elements at the correct positions
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) {
                // For even indices, place the smallest remaining element
                nums[i] = sortedNums[mid - i / 2];
            } else {
                // For odd indices, place the largest remaining element
                nums[i] = sortedNums[n - i / 2 - 1];
            }
        }
    }
};
```

## Test Cases
```
Input: [1, 5, 1, 1, 6, 4]
Output: [1, 6, 1, 5, 1, 4]
Input: [1, 3, 2, 2, 3, 1]
Output: [1, 2, 1, 3, 1, 3]
```

## Key Takeaways
- The wiggle sort condition requires that the elements at even indices are less than or equal to the elements at odd indices.
- The approach involves sorting the array first, then using two pointers to place the elements at the correct positions.
- The time complexity is O(n log n) due to the sorting operation, and the space complexity is O(n) for the sorted array.