# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The length of the input array will be at least 2 and at most 10^5. The input array will contain only non-zero integers. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The approach is to calculate the prefix products and suffix products for each element in the array. We can then multiply these two products to get the product of all elements except the current one. This is done in two passes, one from the start and one from the end of the array.

## Complexity
- Time: O(n)
- Space: O(1) excluding the space required for the output array

## C++ Solution
```cpp
#include <vector>

vector<int> productExceptSelf(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<int> output(n, 1);
    
    // Calculate prefix products
    for (int i = 1; i < n; i++) {
        output[i] = output[i-1] * nums[i-1];
    }
    
    // Calculate suffix products and update output
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
- We can solve this problem in O(n) time complexity without using division.
- The space complexity can be reduced to O(1) by reusing the input array as the output array, but this requires a temporary variable to store the running product.
- The approach can be generalized to handle arrays with zeros, but the problem statement guarantees non-zero integers.