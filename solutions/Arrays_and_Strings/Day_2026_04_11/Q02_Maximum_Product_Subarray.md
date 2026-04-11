# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The array can contain both positive and negative integers. The maximum product subarray is the subarray with the largest product of its elements. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of `24`. The array can be empty, and the maximum product of an empty array is `0`. The length of the array is at most `200` elements.

## Approach
We will use dynamic programming to track the maximum and minimum product up to each position in the array. This is because a negative number can turn a maximum product into a minimum product, and vice versa. We will iterate over the array, updating the maximum and minimum product at each step.

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
        
        int max_product = nums[0];
        int min_product = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                swap(max_product, min_product);
            }
            
            max_product = max(nums[i], max_product * nums[i]);
            min_product = min(nums[i], min_product * nums[i]);
            
            result = max(result, max_product);
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
- A negative number can turn a maximum product into a minimum product, and vice versa.
- The maximum product of an empty array is `0`.