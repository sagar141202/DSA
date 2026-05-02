# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The array can contain duplicates and negative numbers. The length of the array is in the range `[1, 10^5]` and `k` is in the range `[0, 10^5]`.

## Approach
The approach is to use a temporary array to store the rotated elements, then copy them back to the original array. We can also use a more efficient approach using three reversals: reverse the entire array, reverse the first `k` elements, and reverse the rest of the array.

## Complexity
- Time: O(n)
- Space: O(1) for the in-place approach, O(n) for the temporary array approach

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
        
        // Reverse the rest of the array
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
- The key to this problem is to use the modulo operator to calculate the effective number of rotations, which can reduce the number of rotations needed.
- The three-reversal approach is more efficient than the temporary array approach, especially for large arrays.
- The problem can be solved in-place, which means that the original array is modified directly.