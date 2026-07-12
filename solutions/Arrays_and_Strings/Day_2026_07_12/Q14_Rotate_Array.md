# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The array is rotated in-place, meaning that the original array is modified. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array will be `[5, 6, 7, 1, 2, 3, 4]`. The constraints are `1 <= nums.length <= 10^5` and `0 <= k <= 10^5`.

## Approach
The approach is to use a two-step process to rotate the array. First, reverse the entire array, then reverse the first `k` elements and the rest of the array separately. This will result in the array being rotated to the right by `k` steps.

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
        k = k % nums.size(); // handle cases where k > nums.size()
        reverse(nums.begin(), nums.end()); // reverse the entire array
        reverse(nums.begin(), nums.begin() + k); // reverse the first k elements
        reverse(nums.begin() + k, nums.end()); // reverse the rest of the array
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
- The key to solving this problem is to use the two-step reversal process to rotate the array.
- We need to handle cases where `k` is greater than the length of the array by taking the modulus of `k` with the length of the array.
- The time complexity is O(n) because we are reversing the array three times, and each reversal takes O(n) time. The space complexity is O(1) because we are modifying the array in-place.