# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each element `output[i]` is equal to the product of all the numbers in `nums` except `nums[i]`. The constraint is that the solution should not use division and should have a time complexity of O(n). For example, if `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm involves calculating the prefix products and suffix products of the array and then multiplying them to get the product of all numbers except the current number. This approach ensures a time complexity of O(n) and avoids division.

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
    
    // Calculate suffix products and multiply with prefix products
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
```

## Key Takeaways
- We can solve this problem without using division by calculating prefix and suffix products.
- The space complexity can be optimized to O(1) by using the output array to store the prefix products and then updating it with the suffix products.