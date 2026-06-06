# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each `output[i]` is equal to the product of all the numbers in the `nums` array except `nums[i]`. The length of the input array will not exceed `2^31 - 1` and the product of the elements in the array will not exceed `2^31 - 1`. For example, if the input array is `[1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm uses two passes to calculate the product of all numbers to the left and right of each index. It initializes an output array with 1's and then calculates the running product from the left and right. The final output is the product of the left and right arrays.

## Complexity
- Time: O(n)
- Space: O(1) excluding the output array

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> output(n, 1);
    
    // Calculate the running product from the left
    for (int i = 1; i < n; i++) {
        output[i] = output[i - 1] * nums[i - 1];
    }
    
    // Calculate the running product from the right
    int rightProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
        output[i] *= rightProduct;
        rightProduct *= nums[i];
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
- Use two passes to calculate the product of all numbers to the left and right of each index.
- Initialize an output array with 1's to store the running product from the left.
- Calculate the running product from the right and multiply it with the output array to get the final result.