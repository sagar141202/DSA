# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The length of the array `nums` is denoted by `n`, where `1 <= n <= 10^5`. The integer `k` is in the range `[0, 10^5]`.

## Approach
The algorithm uses a temporary array to store the rotated elements. It calculates the effective rotation steps by taking the modulus of `k` with the length of the array `n`. Then, it copies the last `k` elements of the original array to the beginning of the temporary array and the remaining elements to the end of the temporary array.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Calculate the effective rotation steps
        k = k % nums.size();
        
        // Create a temporary array to store the rotated elements
        vector<int> temp(nums.size());
        
        // Copy the last k elements to the beginning of the temporary array
        for (int i = 0; i < k; i++) {
            temp[i] = nums[nums.size() - k + i];
        }
        
        // Copy the remaining elements to the end of the temporary array
        for (int i = k; i < nums.size(); i++) {
            temp[i] = nums[i - k];
        }
        
        // Copy the rotated elements back to the original array
        for (int i = 0; i < nums.size(); i++) {
            nums[i] = temp[i];
        }
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
- The rotation can be performed in-place using a temporary array to store the rotated elements.
- The effective rotation steps are calculated by taking the modulus of `k` with the length of the array `n`.
- The algorithm has a time complexity of O(n) and a space complexity of O(n), where n is the length of the array.