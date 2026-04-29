# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The subarray should contain at least one number. The array can contain both positive and negative numbers. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of `24`. The array can also be empty, in which case the function should return `0`.

## Approach
The approach to solve this problem is to use dynamic programming to track the maximum and minimum product of subarrays ending at each position. This is because a negative number can turn a maximum product into a minimum product, and vice versa. We will maintain two arrays, `max_dp` and `min_dp`, to store the maximum and minimum product of subarrays ending at each position.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int max_so_far = nums[0];
        int min_so_far = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                swap(max_so_far, min_so_far);
            }
            
            max_so_far = max(nums[i], max_so_far * nums[i]);
            min_so_far = min(nums[i], min_so_far * nums[i]);
            
            result = max(result, max_so_far);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: nums = [2,3,-2,4]
Output: 6
Input: nums = [-2,0,-1]
Output: 0
```

## Key Takeaways
- We need to track both the maximum and minimum product of subarrays ending at each position.
- A negative number can turn a maximum product into a minimum product, and vice versa.
- We can solve this problem in O(n) time complexity and O(1) space complexity.