# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each `output[i]` is equal to the product of all the numbers in `nums` except `nums[i]`. The constraint is that the division operation cannot be used, and the output array cannot contain any zeros if the input array does not contain any zeros. For example, given `nums = [1,2,3,4]`, the output should be `[24,12,8,6]` because `24 = 2 * 3 * 4`, `12 = 1 * 3 * 4`, `8 = 1 * 2 * 4`, and `6 = 1 * 2 * 3`. The input array will have at least two elements, and all elements will be 32-bit signed integers.

## Approach
The algorithm involves calculating the prefix products and suffix products for each element in the array. The product of all numbers except the current number is then the product of the prefix product and the suffix product. This approach avoids division and ensures the output array does not contain zeros if the input array does not.

## Complexity
- Time: O(n)
- Space: O(1) excluding the output array, O(n) including the output array

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
    
    // Calculate suffix products and multiply with prefix products
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
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Input: nums = [2,3,4,5]
Output: [60,40,30,24]
```

## Key Takeaways
- We can avoid using division by calculating prefix and suffix products separately.
- The space complexity can be optimized by using the output array to store the prefix products and then updating it with the suffix products in a single pass.
- This approach ensures that the output array does not contain zeros if the input array does not, as required by the problem statement.