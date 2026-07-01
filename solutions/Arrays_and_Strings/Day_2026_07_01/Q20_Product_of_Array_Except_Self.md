# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The solution must not use division and should have a time complexity of O(n). For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm uses two passes through the input array to calculate the prefix and postfix products for each element, then combines these products to find the final result. This approach avoids division and achieves a time complexity of O(n).

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> output(n, 1);
    
    // Calculate prefix products
    for (int i = 1; i < n; i++) {
        output[i] = output[i-1] * nums[i-1];
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
Input: nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
```

## Key Takeaways
- The solution uses two passes through the input array to calculate prefix and postfix products.
- It avoids using division by combining prefix and postfix products to find the final result.
- The time complexity is O(n) and the space complexity is O(1) if the output array is not counted.