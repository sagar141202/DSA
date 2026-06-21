# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. The length of the array is denoted by `n`. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The value of `k` can be larger than `n`, in which case the rotation is performed `k % n` times.

## Approach
The algorithm uses a temporary array to store the rotated elements, then copies them back to the original array. Alternatively, a more efficient approach uses three reversals: reversing the entire array, then reversing the first `k % n` elements, and finally reversing the remaining elements.

## Complexity
- Time: O(n)
- Space: O(1) for the in-place reversal approach, O(n) for the temporary array approach

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Calculate the effective number of rotations
        k = k % nums.size();
        
        // Reverse the entire array
        reverse(nums.begin(), nums.end());
        
        // Reverse the first k elements
        reverse(nums.begin(), nums.begin() + k);
        
        // Reverse the remaining elements
        reverse(nums.begin() + k, nums.end());
    }
};
```

## Test Cases
```
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 7
Output: [1, 2, 3, 4, 5, 6, 7]
```

## Key Takeaways
- The rotation can be performed in-place using three reversals.
- The effective number of rotations is `k % n`, where `n` is the length of the array.
- The time complexity is O(n) for both approaches, but the space complexity is O(1) for the in-place reversal approach and O(n) for the temporary array approach.