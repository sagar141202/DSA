# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each element `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The length of the input array is at least 2 and at most 10,000. All elements in the array are non-zero, and the product of all elements does not exceed 2^31 - 1. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm uses the concept of prefix and postfix products to calculate the product of all elements except the current one. It iterates over the array to calculate the prefix products and then the postfix products. The product of all elements except the current one is the product of the prefix and postfix products.

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
        output[i] = output[i - 1] * nums[i - 1];
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
Input: nums = [2, 3, 4, 5]
Output: [60, 40, 30, 24]
```

## Key Takeaways
- Use prefix and postfix products to avoid division and handle zero elements.
- The space complexity can be optimized to O(1) by using the output array to store the prefix products.
- The time complexity is O(n) due to the two passes over the input array.