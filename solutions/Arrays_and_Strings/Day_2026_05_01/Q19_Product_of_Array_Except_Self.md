# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each element `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The length of the input array will be at least 2 and will be no more than 10,000. The input array will contain at least one zero. The product of all elements in the array will not exceed 2^31 - 1. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The approach involves calculating the prefix products and suffix products for each element in the array. The product of all numbers except the current number is the product of the prefix product and the suffix product. We will use two arrays to store the prefix and suffix products.

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
    
    // Calculate suffix products and update output
    int suffixProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
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
- We can calculate the product of all numbers except the current number by using prefix and suffix products.
- The space complexity can be optimized to O(1) by using the output array to store the prefix products and then updating it with the suffix products.
- The time complexity remains O(n) as we are scanning the array twice.