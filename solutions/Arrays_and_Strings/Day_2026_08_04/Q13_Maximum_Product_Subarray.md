# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the contiguous subarray within the array that has the largest product. The product of an empty subarray is considered to be 0. It is guaranteed that the product of any prefix or suffix of the array does not exceed 2^31 - 1. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of `24`. If the array is `[0,2]`, the maximum product subarray is `[2]` with a product of `2`.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product. We iterate through the array, updating the maximum and minimum product at each step.

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
        
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                swap(maxSoFar, minSoFar);
            }
            
            maxSoFar = max(nums[i], maxSoFar * nums[i]);
            minSoFar = min(nums[i], minSoFar * nums[i]);
            
            result = max(result, maxSoFar);
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
- We must consider both the maximum and minimum product up to each position because a negative number can change the maximum product to a minimum product.
- The space complexity is O(1) because we only use a constant amount of space to store the maximum and minimum product.
- The time complexity is O(n) because we make a single pass through the array.