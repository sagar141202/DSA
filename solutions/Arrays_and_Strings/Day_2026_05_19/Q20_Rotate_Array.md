# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be performed in-place, meaning that the modified array should be stored in the same memory location as the original array. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array should be `[5, 6, 7, 1, 2, 3, 4]`. The array can contain duplicate elements, and `k` can be greater than the length of the array.

## Approach
The algorithm uses a temporary array to store the rotated elements. It calculates the effective rotation steps by taking the modulus of `k` with the length of the array, then copies the last `k` elements to the beginning of the temporary array and the remaining elements to the end of the temporary array.

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
        
        // Create a temporary array
        vector<int> temp(nums.size());
        
        // Copy the last k elements to the beginning of the temporary array
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
```

## Test Cases
```
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 7
Output: [1, 2, 3, 4, 5, 6, 7]
```

## Key Takeaways
- The rotation can be performed in-place by using a temporary array to store the rotated elements.
- The effective rotation steps can be calculated by taking the modulus of `k` with the length of the array, which reduces the number of steps required for the rotation.
- This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the array.