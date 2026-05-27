# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The subarray should contain at least one number. The array can contain both positive and negative numbers, and the maximum product can be obtained by multiplying all the numbers in the subarray. For example, given the array `[-2, 3, -4]`, the maximum product subarray is `[-2, 3, -4]` with a product of `24`. The array can have up to `2 * 10^5` elements, and each element can be in the range `[-10^5, 10^5]`.

## Approach
We will use dynamic programming to track the maximum and minimum product up to each position in the array. This is because a negative number can become maximum by multiplying with another negative number. We will maintain two arrays, `maxDP` and `minDP`, where `maxDP[i]` and `minDP[i]` represent the maximum and minimum product up to index `i` respectively.

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
Output: 0
```

## Key Takeaways
- The maximum product subarray can be obtained by considering the product of all numbers up to each position in the array.
- We need to maintain both the maximum and minimum product up to each position because a negative number can become maximum by multiplying with another negative number.
- The space complexity can be reduced to O(1) by only keeping track of the maximum and minimum product up to the previous position.