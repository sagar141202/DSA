# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each `output[i]` is equal to the product of all the numbers in `nums` except `nums[i]`. The length of the input array will be at least 2 and at most 10^5. Each input element will be between 1 and 10^5. The output array should have the same length as the input array. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The approach involves calculating the product of all numbers to the left of each index and the product of all numbers to the right, then multiplying these two products together. This can be done in a single pass through the array, using two arrays to store the left and right products.

## Complexity
- Time: O(n)
- Space: O(1) (excluding output array)

## C++ Solution
```cpp
#include <vector>

std::vector<int> productExceptSelf(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<int> output(n, 1);
    
    // calculate prefix products
    for (int i = 1; i < n; i++) {
        output[i] = output[i - 1] * nums[i - 1];
    }
    
    // calculate suffix products and update output
    int suffixProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
        output[i] *= suffixProduct;
        suffixProduct *= nums[i];
    }
    
    return output;
}
```

## Test Cases
```
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [2, 3, 4, 5]
Output: [60, 40, 30, 24]
```

## Key Takeaways
- Use dynamic programming to calculate prefix and suffix products in a single pass.
- Initialize the output array with 1s to simplify the calculation of prefix products.
- Update the output array with the product of prefix and suffix products in a second pass.