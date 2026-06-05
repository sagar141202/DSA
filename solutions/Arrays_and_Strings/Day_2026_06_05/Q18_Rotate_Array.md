# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The rotation should be in-place, meaning that the array should be modified directly without creating a new array. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the output should be `[5, 6, 7, 1, 2, 3, 4]`. The array can contain duplicate elements, and `k` can be greater than the length of the array.

## Approach
The approach is to use a temporary array to store the rotated elements, and then copy them back to the original array. We can also use a more efficient approach by using three reversals: reverse the entire array, reverse the first `k` elements, and reverse the rest of the array.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void rotate(vector<int>& nums, int k) {
    // Calculate the effective number of steps to rotate
    k = k % nums.size();
    
    // Reverse the entire array
    reverse(nums.begin(), nums.end());
    
    // Reverse the first k elements
    reverse(nums.begin(), nums.begin() + k);
    
    // Reverse the rest of the array
    reverse(nums.begin() + k, nums.end());
}

// Alternatively, we can use a temporary array
void rotateTemp(vector<int>& nums, int k) {
    int n = nums.size();
    k = k % n;
    vector<int> temp(n);
    
    // Copy the last k elements to the beginning of the temporary array
    for (int i = 0; i < k; i++) {
        temp[i] = nums[n - k + i];
    }
    
    // Copy the rest of the elements to the temporary array
    for (int i = k; i < n; i++) {
        temp[i] = nums[i - k];
    }
    
    // Copy the temporary array back to the original array
    for (int i = 0; i < n; i++) {
        nums[i] = temp[i];
    }
}
```

## Test Cases
```
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Output: [5, 6, 7, 1, 2, 3, 4]
Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 7
Output: [1, 2, 3, 4, 5, 6, 7]
```

## Key Takeaways
- In-place rotation of an array can be achieved using three reversals.
- The effective number of steps to rotate can be calculated by taking the modulus of `k` with the length of the array.
- Using a temporary array can also achieve the rotation, but it requires extra space.