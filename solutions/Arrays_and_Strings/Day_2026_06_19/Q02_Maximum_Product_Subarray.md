# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The product of a subarray is the product of all the integers in the subarray. The array can contain both positive and negative integers. If the array is empty, return 0. For example, given the array `nums = [2,3,-2,4]`, the maximum product subarray is `[2,3,-2,4]` with a product of `24`. However, for `nums = [-2,0,-1]`, the maximum product subarray is `[-1]` with a product of `-1`.

## Approach
We use dynamic programming to track the maximum and minimum product ending at each position, considering the possibility of negative numbers changing the maximum product to minimum and vice versa. The maximum product of a subarray ending at the current position is either the current number itself or the product of the current number and the maximum product ending at the previous position.

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
            if (nums[i] < 0) {
                swap(maxSoFar, minSoFar);
            }
            
            maxSoFar = max(nums[i], maxSoFar * nums[i]);
            minSoFar = min(nums[i], minSoFar * nums[i]);
            
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
Output: -1
```

## Key Takeaways
- The presence of negative numbers can drastically change the maximum product subarray, necessitating the tracking of both maximum and minimum product subarrays.
- Dynamic programming is used to efficiently compute the maximum product subarray by considering all possible subarrays.
- The space complexity is optimized to O(1) by only keeping track of the necessary variables for the dynamic programming approach.