# Product of Array Except Self

## Problem Statement
Given an array of integers `nums`, return an array where each element at index `i` is equal to the product of all numbers in `nums` except the one at index `i`. The length of `nums` is at least 1 and may be up to 2,000. The product of all numbers in `nums` may exceed the maximum limit of an integer. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`, because `24 = 2 * 3 * 4`, `12 = 1 * 3 * 4`, `8 = 1 * 2 * 4`, and `6 = 1 * 2 * 3`.

## Approach
We can solve this problem by using the concept of prefix and postfix products. We calculate the product of all numbers to the left and right of each index and multiply these two products to get the final result. This approach allows us to avoid division and handle large products.

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
        output[i] = output[i - 1] * nums[i - 1];
    }
    
    // Calculate postfix products and update output
    int postfixProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
        output[i] *= postfixProduct;
        postfixProduct *= nums[i];
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
- We can use prefix and postfix products to avoid division and handle large products.
- The time complexity is O(n) because we make two passes over the input array.
- The space complexity is O(1) if we exclude the output array, because we only use a constant amount of extra space to store the prefix and postfix products.