# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that each `output[i]` is equal to the product of all the numbers in `nums` except `nums[i]`. The length of `nums` will be at least 2 and the maximum length will not exceed 10. The product of any prefix or suffix of `nums` will fit in a 32-bit integer. You must solve this problem in-place without using division, and the output array does not count as extra space for space complexity purposes. For example, given `nums = [1,2,3,4]`, the output should be `[24,12,8,6]`.

## Approach
The algorithm involves calculating the prefix products and suffix products separately and then combining them to get the final output. We use two passes through the array to calculate the prefix and suffix products. This approach avoids division and uses constant extra space.

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
        output[i] = output[i-1] * nums[i-1];
    }
    
    // Calculate suffix products and update output
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
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Input: nums = [5,10,15,20]
Output: [3000,1500,1000,750]
```

## Key Takeaways
- We can solve this problem in O(n) time complexity by making two passes through the array.
- The space complexity is O(1) if we exclude the output array, as required by the problem statement.
- This approach avoids division and uses the properties of multiplication to calculate the product of all numbers except the one at each index.