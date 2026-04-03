# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the contiguous subarray within the array that has the largest product. The product of an empty subarray is considered to be 0. It is guaranteed that the product of any contiguous subarray does not exceed 2^31 - 1. For example, given the array `nums = [2,3,-2,4]`, the maximum product subarray is `[2,3,-2,4]` which has a product of `2*3*(-2)*4 = 24`. Another example is `nums = [-2,0,-1]`, the maximum product subarray is `[-2]` or `[-1]` which has a product of `2` or `-1` respectively.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is because a negative number can turn a maximum product into a minimum product and vice versa. By keeping track of both, we can find the maximum product subarray. The intuition is to iterate through the array, updating the maximum and minimum product at each step.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // Initialize the maximum and minimum product
        int maxProductSoFar = nums[0];
        int minProductSoFar = nums[0];
        int result = nums[0];

        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // If the current number is negative, swap max and min product
            if (nums[i] < 0) {
                swap(maxProductSoFar, minProductSoFar);
            }

            // Update max and min product
            maxProductSoFar = max(nums[i], maxProductSoFar * nums[i]);
            minProductSoFar = min(nums[i], minProductSoFar * nums[i]);

            // Update the result
            result = max(result, maxProductSoFar);
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
- The maximum product subarray can be found by keeping track of the maximum and minimum product up to each position in the array.
- A negative number can turn a maximum product into a minimum product and vice versa, so we need to keep track of both.
- The time complexity of this solution is O(n), where n is the number of elements in the array.