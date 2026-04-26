# Rotate Array

## Problem Statement
Given an array of integers `nums` and an integer `k`, rotate the array to the right by `k` steps. The array can be rotated in-place, meaning that the original array is modified to achieve the desired rotation. For example, if `nums = [1, 2, 3, 4, 5, 6, 7]` and `k = 3`, the rotated array would be `[5, 6, 7, 1, 2, 3, 4]`. The rotation should be performed in a way that minimizes the number of operations. The constraints are `1 <= nums.length <= 10^5` and `0 <= k <= 10^5`.

## Approach
The algorithm uses a three-step reversal approach to rotate the array in-place. First, the entire array is reversed, then the first `k` elements are reversed, and finally the remaining elements are reversed. This approach ensures that the array is rotated to the right by `k` steps.

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

Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 7
Output: [1, 2, 3, 4, 5, 6, 7]

Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 10
Output: [4, 5, 6, 7, 1, 2, 3]
```

## Key Takeaways
- The rotation can be achieved by reversing the array three times.
- The effective rotation steps are calculated by taking the modulus of `k` with the length of the array.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it efficient for large arrays.