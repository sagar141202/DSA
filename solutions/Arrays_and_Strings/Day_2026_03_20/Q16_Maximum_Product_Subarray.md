# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The product of a subarray is the product of all elements in the subarray. The problem requires finding the maximum product of any subarray. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of `24`. The array can contain both positive and negative integers, and the maximum product subarray must be a contiguous subset of the array.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product, and vice versa. The maximum product is updated at each position by considering the current number, the product of the current number and the previous maximum product, and the product of the current number and the previous minimum product.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // Initialize max and min product with the first element of the array
        int maxProduct = nums[0];
        int minProduct = nums[0];
        // Initialize the result with the first element of the array
        int result = nums[0];
        
        // Iterate over the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // If the current number is negative, swap max and min product
            if (nums[i] < 0) {
                swap(maxProduct, minProduct);
            }
            // Update max and min product
            maxProduct = max(nums[i], maxProduct * nums[i]);
            minProduct = min(nums[i], minProduct * nums[i]);
            // Update the result
            result = max(result, maxProduct);
        }
        return result;
    }
};
```

## Test Cases
```
Input: nums = [2,3,-2,4]
Output: 6
Input: nums = [-2,0,-1]
Output: 0
```

## Key Takeaways
- The algorithm must track both the maximum and minimum product up to each position in the array.
- A negative number can turn a maximum product into a minimum product, and vice versa.
- The space complexity is O(1) because only a constant amount of space is used to store the maximum and minimum product, and the result.