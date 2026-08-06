# Rotate Array

## Problem Statement
Given an array of integers and an integer k, rotate the array to the right by k steps. The rotation should be performed in-place, meaning that the original array should be modified to reflect the rotation. For example, if the input array is [1, 2, 3, 4, 5, 6, 7] and k = 3, the rotated array should be [5, 6, 7, 1, 2, 3, 4]. The input array will contain at least one element and at most 10^5 elements. The value of k will be in the range [0, 10^5].

## Approach
The algorithm involves using three reversals to rotate the array in-place. First, reverse the entire array, then reverse the first k elements, and finally reverse the rest of the array. This approach ensures that the rotation is performed efficiently and correctly.

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
        // Calculate the actual number of steps to rotate
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

Input: nums = [1, 2], k = 3
Output: [2, 1]
```

## Key Takeaways
- The rotation can be performed in-place using three reversals.
- The actual number of steps to rotate is k % n, where n is the size of the array.
- The reverse function from the C++ Standard Library can be used to reverse the array or parts of it.