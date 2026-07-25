# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The array can contain both positive and negative numbers. The length of the array is at least 1 and at most 200. The elements of the array are at least -128 and at most 128. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of `24`. Another example is the array `[1, -2, -3, 0, 7, -8, -2]`, where the maximum product subarray is `[-2, -3, 0, 7, -8, -2]` is not the correct answer, the correct answer is `7` since `7` itself is a subarray with the maximum product.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product and vice versa. We initialize two variables, `max_product` and `min_product`, to the first element of the array and then iterate through the rest of the array, updating these variables at each step.

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
        if (nums.empty()) {
            return 0;
        }

        int max_product = nums[0];
        int min_product = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                std::swap(max_product, min_product);
            }

            max_product = std::max(nums[i], max_product * nums[i]);
            min_product = std::min(nums[i], min_product * nums[i]);

            result = std::max(result, max_product);
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
Input: nums = [1, -2, -3, 0, 7, -8, -2]
Output: 7
```

## Key Takeaways
- We must consider the impact of negative numbers on the product of a subarray.
- Dynamic programming is used to efficiently track the maximum and minimum product up to each position in the array.
- The maximum product of a subarray can be the product of a single element, so we need to consider individual elements as potential maximum product subarrays.