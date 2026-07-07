# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the contiguous subarray within the array that has the largest product. The subarray should contain at least one number. The input array can contain both positive and negative numbers, and the maximum product can be either positive or negative. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of `24`. The array can have a maximum length of `20000` and each element can be in the range of `-10^5` to `10^5`.

## Approach
We can solve this problem using dynamic programming, keeping track of the maximum and minimum product up to each position in the array. This is because a negative number can turn a maximum product into a minimum product. We initialize `max_product` and `min_product` with the first element of the array and then iterate through the array, updating these values at each step.

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
- The maximum product subarray can start at any position in the array, not just at the beginning.
- We need to keep track of both the maximum and minimum product up to each position because a negative number can turn a maximum product into a minimum product.
- The time complexity is linear, making this solution efficient for large inputs.