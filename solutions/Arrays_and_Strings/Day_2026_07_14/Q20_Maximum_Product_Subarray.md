# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The array can contain both positive and negative numbers. The length of the array is at most 20000. For example, given the array `[-2,0,-1]`, the maximum product subarray is `[-2,-1]` which has a product of 2.

## Approach
The approach to solve this problem is to use dynamic programming to track the maximum and minimum product up to each position. This is because a negative number can turn a maximum product into a minimum product. We initialize two variables, `max_product` and `min_product`, to the first element of the array and then iterate through the array, updating these variables at each step.

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
            // If the current number is negative, swap max_product and min_product
            if (nums[i] < 0) {
                swap(max_product, min_product);
            }
            
            // Update max_product and min_product
            max_product = max(nums[i], max_product * nums[i]);
            min_product = min(nums[i], min_product * nums[i]);
            
            // Update the result
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
- We need to track both the maximum and minimum product up to each position because a negative number can turn a maximum product into a minimum product.
- We update the maximum and minimum product at each step by considering the current number and the product of the current number with the previous maximum and minimum product.
- The result is the maximum of the maximum product at each position.