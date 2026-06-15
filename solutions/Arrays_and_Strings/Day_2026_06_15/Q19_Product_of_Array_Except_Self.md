# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each element `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The length of the input array will be at least 2 and will not exceed 10^5. The input array will only contain integers between -100 and 100. The output array should not use division and should have a time complexity of O(n).

## Approach
The algorithm uses two passes through the array to compute the product of all numbers to the left and right of each index. It then combines these two products to get the final result.

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
        std::vector<int> output(n, 1);
        
        // Compute product of all numbers to the left
        for (int i = 1; i < n; i++) {
            output[i] = output[i-1] * nums[i-1];
        }
        
        // Compute product of all numbers to the right and combine
        int rightProduct = 1;
        for (int i = n - 1; i >= 0; i--) {
            output[i] *= rightProduct;
            rightProduct *= nums[i];
        }
        
        return output;
    }
};
```

## Test Cases
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Input: nums = [5, 10, 15, 20]
Output: [3000,1500,1000,750]
```

## Key Takeaways
- The solution avoids division by using two passes to compute the product of all numbers to the left and right of each index.
- The space complexity is O(1) if we exclude the space needed for the output array, as required by the problem statement.
- The time complexity is O(n) because we make two passes through the array.