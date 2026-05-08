# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The length of the input array will be at least 2 and will not exceed 10^5. The input array will only contain integers between -10^5 and 10^5. The output array should not contain any zeros. For example, given the input array `[1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm uses the concept of prefix and postfix products to calculate the product of all elements except the current one. It initializes two arrays, `prefix` and `postfix`, to store the cumulative product of elements from the start and end of the array respectively. The final result is obtained by multiplying the corresponding elements of `prefix` and `postfix` arrays.

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
    
    // Calculate postfix products and update output
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
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

## Key Takeaways
- The solution has a time complexity of O(n) and a space complexity of O(1) (excluding the output array) by utilizing the output array to store the prefix products.
- The algorithm avoids division by using the prefix and postfix product approach, making it more efficient and robust.
- The solution handles edge cases such as zero and negative numbers correctly.