# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified to reflect the rotation. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The array can contain duplicate elements, and `k` can be greater than the length of the array. In such cases, the rotation should be performed by taking the remainder of `k` divided by the length of the array.

## Approach
The approach is to use a temporary array to store the rotated elements. We can calculate the new index of each element by adding `k` to its current index and taking the modulus of the length of the array. This ensures that the rotation wraps around to the beginning of the array when necessary.

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
        // Calculate the effective rotation steps by taking the modulus of k
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

Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 10
Output: [5, 6, 7, 1, 2, 3, 4]
```

## Key Takeaways
- The rotation can be performed in-place by using a temporary array to store the rotated elements.
- The effective rotation steps can be calculated by taking the modulus of `k` divided by the length of the array.
- The solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the array.