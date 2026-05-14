# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The subarray should contain at least one number. The array can contain both positive and negative numbers, and the product of two negative numbers can result in a positive number.

## Approach
We will use dynamic programming to track the maximum and minimum product up to each position in the array. This is because a negative number can turn a maximum product into a minimum product and vice versa. We will maintain two arrays, `max_dp` and `min_dp`, to store the maximum and minimum product up to each position.

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
        if (nums.empty()) {
            return 0;
        }
        
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
- We need to track both the maximum and minimum product up to each position in the array.
- A negative number can turn a maximum product into a minimum product and vice versa, so we need to swap `max_so_far` and `min_so_far` when we encounter a negative number.
- We can solve this problem in O(n) time complexity and O(1) space complexity.