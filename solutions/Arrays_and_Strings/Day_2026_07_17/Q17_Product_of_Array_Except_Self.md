# Product of Array Except Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` is the product of all numbers in the input array except the one at `i`. The constraint is that we cannot use the division operator. For example, if the input array is `[1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`. The input array will contain at least one element and at most 1000 elements, and all elements will be in the range of 32-bit signed integers.

## Approach
The algorithm uses dynamic programming to calculate the product of all elements to the left and right of each index. It iterates through the array twice, once from left to right and once from right to left, to calculate the prefix and postfix products. The product of all elements except the one at each index is then calculated by multiplying the corresponding prefix and postfix products.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

std::vector<int> productExceptSelf(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<int> output(n, 1);
    
    // Calculate prefix products
    for (int i = 1; i < n; i++) {
        output[i] = output[i - 1] * nums[i - 1];
    }
    
    // Calculate postfix products and update output
    int postfix = 1;
    for (int i = n - 1; i >= 0; i--) {
        output[i] *= postfix;
        postfix *= nums[i];
    }
    
    return output;
}
```

## Test Cases
```
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [5, 10, 15, 20]
Output: [3000, 1500, 1000, 750]
```

## Key Takeaways
- We can calculate the product of all elements except the one at each index by using prefix and postfix products.
- We can avoid using the division operator by using dynamic programming to calculate the prefix and postfix products.
- The space complexity can be optimized to O(1) by using the output array to store the prefix products and a variable to store the postfix product.