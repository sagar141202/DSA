# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each element `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The constraint is that we cannot use division, and the output array should be of the same length as the input array. For example, if `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
We can use a two-pass approach, first calculating the prefix products and then the suffix products. This allows us to calculate the product of all elements except the current one in linear time. We initialize two arrays, `prefix` and `suffix`, where `prefix[i]` is the product of all numbers from index 0 to `i-1`, and `suffix[i]` is the product of all numbers from index `i+1` to the end.

## Complexity
- Time: O(n)
- Space: O(1) excluding output space, O(n) including output space

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
    
    // Calculate suffix products and multiply with prefix products
    int suffixProduct = 1;
    for (int i = n-1; i >= 0; i--) {
        output[i] *= suffixProduct;
        suffixProduct *= nums[i];
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
- Use of prefix and suffix products to avoid division.
- Two-pass approach to calculate the product of all elements except the current one in linear time.
- Space complexity can be optimized by using output array to store prefix products and then updating it with suffix products.