# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the original array should be modified. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The array can contain duplicate elements and the rotation count `k` can be larger than the length of the array.

## Approach
The algorithm uses a temporary array to store the rotated elements, then copies them back to the original array. This approach ensures that the rotation is performed in-place and efficiently. The key insight is to use the modulo operator to handle cases where `k` is larger than the length of the array.

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
        // Calculate the effective rotation count
        k = k % nums.size();
        
        // Create a temporary array to store the rotated elements
        vector<int> temp(nums.size());
        
        // Copy the last k elements to the beginning of the temporary array
        for (int i = 0; i < k; i++) {
            temp[i] = nums[nums.size() - k + i];
        }
        
        // Copy the remaining elements to the temporary array
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
```

## Key Takeaways
- Use the modulo operator to handle cases where `k` is larger than the length of the array.
- Create a temporary array to store the rotated elements, then copy them back to the original array.
- The rotation can be performed in-place using a single pass through the array.