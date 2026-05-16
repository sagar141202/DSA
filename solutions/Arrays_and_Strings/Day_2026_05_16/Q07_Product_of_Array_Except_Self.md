# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each element `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The length of the input array will not exceed `10^4`, and the input array will contain only integers in the range `[-9, 9]`. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm involves initializing two arrays, `prefix` and `suffix`, to store the cumulative product of elements from the start and end of the array respectively. Then, we multiply corresponding elements from `prefix` and `suffix` to get the product of all elements except the current one.

## Complexity
- Time: O(n)
- Space: O(1) (excluding the output array)

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
    
    // calculate suffix products and update output
    int suffix = 1;
    for (int i = n - 1; i >= 0; i--) {
        output[i] *= suffix;
        suffix *= nums[i];
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
- Use prefix and suffix arrays to efficiently calculate the product of all elements except the current one.
- The space complexity can be optimized to O(1) by using the output array to store the prefix products and a variable to store the suffix product.