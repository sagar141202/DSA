# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The constraint is that we cannot use the division operator and the solution should have a time complexity of less than O(n^2). For example, if the input is `[1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
We can solve this problem by calculating the prefix products and suffix products for each element in the array. The product of all elements except the current element can be calculated by multiplying the prefix product and suffix product. This approach allows us to avoid using the division operator and achieve a time complexity of O(n).

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> output(n);
        
        // Calculate prefix products
        output[0] = 1;
        for (int i = 1; i < n; i++) {
            output[i] = output[i-1] * nums[i-1];
        }
        
        // Calculate suffix products and update output
        int suffixProduct = 1;
        for (int i = n-1; i >= 0; i--) {
            output[i] *= suffixProduct;
            suffixProduct *= nums[i];
        }
        
        return output;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [2, 3, 4, 5]
Output: [60, 40, 30, 24]
```

## Key Takeaways
- We can solve this problem without using the division operator by calculating prefix and suffix products.
- The time complexity of this solution is O(n), where n is the number of elements in the input array.
- The space complexity of this solution is O(1), excluding the space required for the output array.