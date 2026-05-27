# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that `output[i]` is equal to the product of all the numbers in the input array except `nums[i]`. The length of the input array will not exceed 10,000. The input array will have at least two elements. The input array will only contain non-zero integers. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm uses the concept of prefix and postfix products to calculate the product of all numbers except the current one. It initializes two arrays, `prefix` and `postfix`, where `prefix[i]` stores the product of all numbers from index 0 to `i-1` and `postfix[i]` stores the product of all numbers from index `i+1` to `n-1`. The result is then calculated by multiplying the corresponding `prefix` and `postfix` values.

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
    
    // Calculate postfix products and multiply with prefix products
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
Input: nums = [5, 10, 15, 20]
Output: [3000, 1500, 1000, 750]
```

## Key Takeaways
- The algorithm avoids division to handle cases where the input array contains zeros.
- It uses a single output array to store both prefix and postfix products, reducing space complexity.
- The time complexity remains linear, making it efficient for large input arrays.