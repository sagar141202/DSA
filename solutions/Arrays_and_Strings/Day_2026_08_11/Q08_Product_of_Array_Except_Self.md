# Product of Array Except Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` is the product of all numbers in the input array except the one at `i`. The constraint is that the output array cannot contain any zeros if the input array contains a zero. For example, given the input `[1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`. If the input array contains a zero, the output array should contain zeros except at the index where the zero is present in the input array, which should be the product of all other numbers.

## Approach
The algorithm uses the concept of prefix and postfix products to calculate the product of all numbers except the one at each index. It initializes two arrays, one for prefix products and one for postfix products, and then combines them to get the final result.

## Complexity
- Time: O(n)
- Space: O(1), excluding the space required for the output array

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
    
    // Calculate postfix products and update output array
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
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [0, 1, 2, 3]
Output: [6, 0, 0, 0]
```

## Key Takeaways
- The algorithm has a linear time complexity due to the use of prefix and postfix products.
- The space complexity can be optimized to O(1) by using the output array to store the prefix products and then updating it with the postfix products.
- The solution handles the case where the input array contains zeros by using the property that the product of all numbers except the one at index `i` will be zero if the input array contains a zero at any index other than `i`.