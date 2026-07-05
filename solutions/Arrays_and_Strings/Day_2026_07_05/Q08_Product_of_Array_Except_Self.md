# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each element `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The constraint is that the division operation is not allowed. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`, because `24 = 2 * 3 * 4`, `12 = 1 * 3 * 4`, `8 = 1 * 2 * 4`, and `6 = 1 * 2 * 3`.

## Approach
The algorithm uses the concept of prefix and postfix products to calculate the product of all elements except the current one. It initializes two arrays, `prefix` and `postfix`, where `prefix[i]` stores the product of all numbers from index `0` to `i-1`, and `postfix[i]` stores the product of all numbers from index `i+1` to `n-1`. The final result for each index `i` is the product of `prefix[i]` and `postfix[i]`.

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
    
    // calculate prefix products
    for (int i = 1; i < n; i++) {
        output[i] = output[i-1] * nums[i-1];
    }
    
    // calculate postfix products and update output
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
- The solution avoids division by utilizing prefix and postfix products.
- It achieves O(n) time complexity by making two passes through the input array.
- The space complexity is O(1) if we exclude the space required for the output array, as we only use a constant amount of space to store the prefix and postfix products.