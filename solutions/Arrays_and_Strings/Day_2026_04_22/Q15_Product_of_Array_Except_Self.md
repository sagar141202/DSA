# Product of Array Except Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` is the product of all numbers in the input array except the one at `i`. The length of the input array will be at least 1 and not more than 20,000. The input array can contain 0's, but the output array cannot contain 0's. If the input array contains a 0, then the output array will contain a 0 at the same index. The input array does not contain any other zeros. For example, given the input array `[1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The approach is to calculate the prefix product and suffix product for each index and multiply them to get the product of all numbers except the one at that index. This can be done in two passes through the array.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n, 1);
    
    // calculate prefix product
    for (int i = 1; i < n; i++) {
        res[i] = res[i-1] * nums[i-1];
    }
    
    // calculate suffix product and multiply with prefix product
    int suffix = 1;
    for (int i = n-1; i >= 0; i--) {
        res[i] *= suffix;
        suffix *= nums[i];
    }
    
    return res;
}
```

## Test Cases
```
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [5, 2, 3, 4]
Output: [24, 60, 40, 30]
```

## Key Takeaways
- We use two passes through the array to calculate the prefix and suffix products.
- The space complexity is O(1) if we don't count the output array, as we only use a constant amount of space.
- The time complexity is O(n) as we make two passes through the array.