# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The subarray should contain at least one number. The array can contain both positive and negative numbers, and the maximum product can be achieved by multiplying all the numbers in the subarray.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product. We initialize `max_product` and `min_product` to the first element of the array and then iterate through the array, updating these values based on the current element.

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
- We need to track both the maximum and minimum product up to each position in the array.
- A negative number can turn a maximum product into a minimum product, so we need to swap `max_product` and `min_product` when we encounter a negative number.
- The result is the maximum of the `max_product` values at each position in the array.