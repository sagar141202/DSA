# Product of Array Except Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` is the product of all numbers in the input array except the one at `i`. The solution should not use division and should have a time complexity of O(n). For example, if the input is `[1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`. The input array will contain at least one element and at most 1000 elements, each in the range of -1000 to 1000.

## Approach
The algorithm uses two passes through the array to calculate the prefix and postfix products. It initializes two arrays, one for prefix products and one for postfix products, then combines these to get the final result. This approach avoids division and achieves the required time complexity.

## Complexity
- Time: O(n)
- Space: O(1) excluding the output array, or O(n) including it

## C++ Solution
```cpp
#include <vector>

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> output(n, 1);
    
    // Calculate prefix products
    for (int i = 1; i < n; ++i) {
        output[i] = output[i - 1] * nums[i - 1];
    }
    
    // Calculate postfix products and update output
    int postfix = 1;
    for (int i = n - 1; i >= 0; --i) {
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
Input: [5, 10, 15, 20]
Output: [3000, 1500, 1000, 750]
```

## Key Takeaways
- We can solve this problem without using division by calculating prefix and postfix products separately.
- The space complexity can be optimized by using the output array to store the prefix products, thus avoiding the need for an additional array.
- This approach scales linearly with the size of the input array, making it efficient for large inputs.