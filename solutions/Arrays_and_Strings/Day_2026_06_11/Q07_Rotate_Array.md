# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The array can be rotated in-place, and `k` can be greater than the length of the array. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array would be `[5, 6, 7, 1, 2, 3, 4]`. The function should return the rotated array.

## Approach
The algorithm uses a three-step reverse approach to rotate the array in-place. First, reverse the entire array, then reverse the first `k` elements, and finally reverse the remaining elements.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // calculate the effective number of steps to rotate
        k = k % nums.size();
        
        // reverse the entire array
        reverse(nums.begin(), nums.end());
        
        // reverse the first k elements
        reverse(nums.begin(), nums.begin() + k);
        
        // reverse the remaining elements
        reverse(nums.begin() + k, nums.end());
    }
};
```

## Test Cases
```
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Input: nums = [-1, -100, 3, 99], k = 2
Output: [3, 99, -1, -100]
```

## Key Takeaways
- The key to solving this problem is to use the three-step reverse approach to rotate the array in-place.
- The effective number of steps to rotate is `k % n`, where `n` is the length of the array, to handle cases where `k` is greater than `n`.
- The `reverse` function is used to reverse the array and its sub-arrays.