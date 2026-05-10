# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each element `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The length of the input array is at least 2 and at most 5 * 10^4. Each element `nums[i]` is at least -10^9 and at most 10^9. It is guaranteed that the product of all the elements of `nums` does not exceed 10^9. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm uses the concept of prefix and postfix products to calculate the product of all elements except the current element. It initializes two arrays, `prefix` and `postfix`, where `prefix[i]` stores the product of all elements before `i` and `postfix[i]` stores the product of all elements after `i`. The final result is obtained by multiplying the corresponding elements of `prefix` and `postfix` arrays.

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
Input: nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

## Key Takeaways
- The solution uses the concept of prefix and postfix products to avoid division and handle zero values.
- It achieves a time complexity of O(n) by iterating through the array twice.
- The space complexity is O(1) excluding the output array, as it only uses a constant amount of space to store the postfix product.