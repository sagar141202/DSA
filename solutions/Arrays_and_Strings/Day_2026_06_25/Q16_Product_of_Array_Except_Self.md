# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each element `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The length of the input array will not exceed 10,000. The input array will contain at least two elements and the elements will be in the range [-100, 100]. The output array should not contain any zeros. For example, if the input array is `[1, 2, 3, 4]`, the output array should be `[24, 12, 8, 6]`.

## Approach
The algorithm uses the concept of prefix and postfix products to calculate the product of all elements except the current element. It initializes two arrays, `prefix` and `postfix`, where `prefix[i]` stores the product of all elements before index `i` and `postfix[i]` stores the product of all elements after index `i`. The final output is calculated by multiplying the corresponding `prefix` and `postfix` values.

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
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [2, 3, 4, 5]
Output: [60, 40, 30, 24]
```

## Key Takeaways
- Use prefix and postfix products to avoid division and handle zero values.
- Optimize space complexity by using a single output array to store prefix and final products.
- Initialize the output array with ones to simplify the prefix product calculation.