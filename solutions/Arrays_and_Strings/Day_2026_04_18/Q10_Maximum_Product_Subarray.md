# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The subarray should contain at least one number. The array can contain both positive and negative numbers. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of `24`. The array can also be empty, in which case the function should return `0`. The length of the array is at most `20000` and all elements are in the range `[-10^5, 10^5]`.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can become the maximum product if multiplied by another negative number. The maximum product is updated at each step if the current product is greater.

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
Input: [-2,3,-4]
Output: 24
Input: [1, -2, 3, 0, -4, -5]
Output: 24
Input: [0, 2]
Output: 2
```

## Key Takeaways
- The maximum product subarray can be found by tracking the maximum and minimum product up to each position.
- A negative number can become the maximum product if multiplied by another negative number.
- Dynamic programming is used to solve this problem efficiently.