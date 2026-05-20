# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each `output[i]` is equal to the product of all the numbers in the `nums` array except `nums[i]`. The problem statement has the following constraints: the length of the input array `nums` is at least 2 and at most 10^5, and each element in `nums` is a 32-bit signed integer. The output array should have the same length as the input array. For example, given the input `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm uses the concept of prefix and postfix products to calculate the product of all numbers except the current number. It initializes two arrays, one for prefix products and one for postfix products, then combines these to obtain the final result. The approach ensures that each number in the output array is the product of all numbers in the input array except the number at the corresponding index.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> output(n);
    
    // calculate prefix products
    output[0] = 1;
    for (int i = 1; i < n; i++) {
        output[i] = output[i-1] * nums[i-1];
    }
    
    // calculate postfix products and update output
    int postfix = 1;
    for (int i = n-1; i >= 0; i--) {
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
- The solution avoids division by calculating prefix and postfix products separately.
- It uses a single output array to store both the prefix products and the final result, minimizing space complexity.
- The algorithm has a linear time complexity due to the two passes over the input array.