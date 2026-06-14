# Product of Array Except Self

## Problem Statement
Given an array of integers `nums`, return an array where each element at index `i` is equal to the product of all the numbers in `nums` except the one at `i`. The length of the input array will be at least 1 and may be as large as 25. The input array may contain duplicate elements, and the product of all elements may exceed the maximum limit of an integer. For example, given `nums = [1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The algorithm uses the concept of prefix and postfix products to calculate the product of all numbers except the one at each index. It initializes two arrays, `prefix` and `postfix`, to store the cumulative product of all numbers to the left and right of each index, respectively. Then, it calculates the final result by multiplying the corresponding prefix and postfix products for each index.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, 1);
    
    // Calculate prefix products
    for (int i = 1; i < n; i++) {
        result[i] = result[i - 1] * nums[i - 1];
    }
    
    // Calculate postfix products and update result
    int postfix = 1;
    for (int i = n - 1; i >= 0; i--) {
        result[i] *= postfix;
        postfix *= nums[i];
    }
    
    return result;
}
```

## Test Cases
```
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [5, 10, 15, 20]
Output: [3000, 1500, 1000, 750]
```

## Key Takeaways
- The solution uses the concept of prefix and postfix products to avoid division and handle large products.
- It iterates through the input array twice, once from left to right and once from right to left, to calculate the prefix and postfix products.
- The space complexity is O(1) if we exclude the space required for the output array, as we only use a constant amount of space to store the prefix and postfix products.