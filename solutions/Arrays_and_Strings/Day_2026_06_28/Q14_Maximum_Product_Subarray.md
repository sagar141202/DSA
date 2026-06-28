# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the contiguous subarray within the array that has the largest product. The product of an empty subarray is considered to be 0. It is guaranteed that the product of any subarray does not exceed 2^31 - 1. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` which has a product of `24`. Another example is the array `[1, -2, 3, 0, -1]`, where the maximum product subarray is `[1, -2, 3]` with a product of `6`.

## Approach
The algorithm uses dynamic programming to keep track of the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product and vice versa. The maximum product at each position is the maximum of the current number, the product of the current number and the previous maximum product, and the product of the current number and the previous minimum product.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxProduct(std::vector<int>& nums) {
        if (nums.empty()) return 0;
        
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                std::swap(maxSoFar, minSoFar);
            }
            
            maxSoFar = std::max(nums[i], maxSoFar * nums[i]);
            minSoFar = std::min(nums[i], minSoFar * nums[i]);
            
            result = std::max(result, maxSoFar);
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
- The algorithm must consider both the maximum and minimum product up to each position because a negative number can change the maximum product to a minimum product and vice versa.
- The time complexity is linear because we only need to traverse the array once.
- The space complexity is constant because we only use a constant amount of space to store the maximum and minimum product.