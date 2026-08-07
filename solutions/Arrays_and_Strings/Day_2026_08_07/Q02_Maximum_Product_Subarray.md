# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The product of an empty subarray is considered to be 0. The array can contain both positive and negative integers. For example, given the array `nums = [2,3,-2,4]`, the maximum product subarray is `[2,3,-2,4]` with a product of `24`. However, for the array `nums = [-2,0,-1]`, the maximum product subarray is `[-1]` with a product of `-1`.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product. The maximum product at each position is the maximum of the current number and the product of the current number with the maximum product at the previous position.

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
        if (nums.empty()) return 0;
        
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            int temp = maxSoFar;
            maxSoFar = max(nums[i], max(maxSoFar * nums[i], minSoFar * nums[i]));
            minSoFar = min(nums[i], min(temp * nums[i], minSoFar * nums[i]));
            result = max(result, maxSoFar);
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
- The maximum product subarray can start at any position in the array, not just at the beginning.
- A negative number can turn a maximum product into a minimum product, so we need to track both the maximum and minimum product up to each position.
- The space complexity is O(1) because we only use a constant amount of space to store the maximum and minimum product at each position.