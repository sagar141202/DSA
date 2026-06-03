# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The product of a subarray is the product of all the integers in the subarray. The array can contain both positive and negative integers. The length of the array is at least 1 and at most 200. The range of the integers in the array is between -10^5 and 10^5 (inclusive). For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of 24.

## Approach
The approach involves iterating through the array while keeping track of the maximum and minimum product up to each position. This is because a negative number can turn a maximum product into a minimum product and vice versa. We update the maximum product at each step and return it at the end.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // Initialize max and min product
        int maxProd = nums[0];
        int minProd = nums[0];
        int result = nums[0];
        
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // If the current number is negative, swap maxProd and minProd
            if (nums[i] < 0) {
                swap(maxProd, minProd);
            }
            
            // Update maxProd and minProd
            maxProd = max(nums[i], maxProd * nums[i]);
            minProd = min(nums[i], minProd * nums[i]);
            
            // Update the result
            result = max(result, maxProd);
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
- The key to solving this problem is to keep track of both the maximum and minimum product up to each position.
- We need to handle the case where the current number is negative by swapping the maximum and minimum product.
- The time complexity is O(n) because we only iterate through the array once.