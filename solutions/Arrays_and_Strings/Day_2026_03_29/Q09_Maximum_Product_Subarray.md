# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The product of a subarray is the product of all the integers in the subarray. The array can contain both positive and negative integers, and the product of two negative numbers is a positive number. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3]` with a product of `6`, but if the array is `[-4,-3,-2]`, the maximum product subarray is `[-4,-3]` or `[-3,-2]` with a product of `12`. The input array `nums` will have a length of at least `1` and at most `200`.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product. By keeping track of both the maximum and minimum product, we can handle negative numbers correctly. The maximum product of a subarray ending at the current position is either the current number itself or the product of the current number and the maximum product of the subarray ending at the previous position.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int maxProduct(vector<int>& nums) {
    // Initialize the maximum and minimum product up to the current position
    int max_product = nums[0];
    int min_product = nums[0];
    // Initialize the result
    int result = nums[0];
    
    // Iterate over the array starting from the second element
    for (int i = 1; i < nums.size(); i++) {
        // If the current number is negative, swap max_product and min_product
        if (nums[i] < 0) {
            swap(max_product, min_product);
        }
        
        // Update max_product and min_product
        max_product = max(nums[i], max_product * nums[i]);
        min_product = min(nums[i], min_product * nums[i]);
        
        // Update the result
        result = max(result, max_product);
    }
    
    return result;
}
```

## Test Cases
```
Input: nums = [2,3,-2,4]
Output: 6
Input: nums = [-2,0,-1]
Output: 0
Input: nums = [0,2]
Output: 2
```

## Key Takeaways
- Keep track of both the maximum and minimum product up to each position in the array to handle negative numbers correctly.
- Use dynamic programming to efficiently compute the maximum product of a subarray.
- The maximum product of a subarray can start at any position in the array, so we need to consider all possible starting positions.