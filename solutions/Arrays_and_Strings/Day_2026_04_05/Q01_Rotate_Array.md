# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the array should be modified directly without creating a new array. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The array can contain duplicate elements, and `k` can be greater than the length of the array.

## Approach
The approach is to use a temporary array to store the last `k` elements of the original array, then shift the remaining elements to the right, and finally copy the elements from the temporary array to the beginning of the original array. Alternatively, we can use a reverse algorithm to reverse the entire array, then reverse the first `k` elements and the remaining elements separately.

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
        // calculate the effective rotation steps
        k = k % nums.size();
        
        // reverse the entire array
        reverse(nums.begin(), nums.end());
        
        // reverse the first k elements
        reverse(nums.begin(), nums.begin() + k);
        
        // reverse the remaining elements
        reverse(nums.begin() + k, nums.end());
    }
};

// alternative solution using a temporary array
class Solution2 {
public:
    void rotate(vector<int>& nums, int k) {
        // calculate the effective rotation steps
        k = k % nums.size();
        
        // create a temporary array to store the last k elements
        vector<int> temp(nums.end() - k, nums.end());
        
        // shift the remaining elements to the right
        for (int i = nums.size() - k - 1; i >= 0; i--) {
            nums[i + k] = nums[i];
        }
        
        // copy the elements from the temporary array to the beginning
        for (int i = 0; i < k; i++) {
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
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 10
Output: [4, 5, 6, 7, 1, 2, 3]
```

## Key Takeaways
- The rotation can be performed in-place using a temporary array or by reversing the array.
- The effective rotation steps can be calculated by taking the modulus of `k` with the length of the array.
- The reverse algorithm can be used to reverse the entire array and then reverse the first `k` elements and the remaining elements separately.