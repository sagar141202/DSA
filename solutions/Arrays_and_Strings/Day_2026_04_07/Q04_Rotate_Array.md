# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The length of the array is `n`. If `k` is greater than `n`, the effective number of steps is `k % n`. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the output should be `[5, 6, 7, 1, 2, 3, 4]`. If `k` is negative, rotate the array to the left by `abs(k)` steps.

## Approach
The algorithm uses a temporary array to store the rotated elements. It calculates the effective rotation steps by taking the modulus of `k` with the length of the array. Then, it copies the last `k` elements of the original array to the beginning of the temporary array and the remaining elements to the end of the temporary array.

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
        
        // Copy the last k elements of the original array to the beginning of the temporary array
        for (int i = 0; i < k; i++) {
            temp[i] = nums[nums.size() - k + i];
        }
        
        // Copy the remaining elements to the end of the temporary array
        for (int i = k; i < nums.size(); i++) {
            temp[i] = nums[i - k];
        }
        
        // Copy the temporary array back to the original array
        nums = temp;
    }
};

// In-place solution without using extra space
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // Calculate the effective rotation steps
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

Input: nums = [1, 2, 3, 4, 5, 6, 7], k = -3
Output: [4, 5, 6, 7, 1, 2, 3]
```

## Key Takeaways
- The rotation can be done in-place without using extra space by reversing the array three times.
- The effective rotation steps can be calculated by taking the modulus of `k` with the length of the array.
- The problem can be solved using a temporary array to store the rotated elements.