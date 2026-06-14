# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The array can contain both positive and negative integers. The maximum product subarray is the subarray with the largest product of its elements. For example, given the array `nums = [2,3,-2,4]`, the maximum product subarray is `[2,3]` which has a product of `6`. However, if the array is `nums = [-2,0,-1]`, the maximum product subarray is `[-1]` or `[-2]` which has a product of `-1` or `-2` respectively, but since `-1` is greater than `-2`, the answer is `-1`.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product. We initialize `max_product` and `min_product` with the first element of the array and then iterate through the rest of the array, updating these variables based on the current element.

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
Output: -1
```

## Key Takeaways
- The algorithm must consider both the maximum and minimum product up to each position due to the presence of negative numbers.
- The time complexity is linear because we only need to make a single pass through the array.
- The space complexity is constant because we only use a fixed amount of space to store the maximum and minimum product.