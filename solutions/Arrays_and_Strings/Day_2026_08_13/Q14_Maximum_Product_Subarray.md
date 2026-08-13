# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The subarray must contain at least one number. The array can contain both positive and negative numbers, and the maximum product can be obtained by multiplying all the numbers in the subarray. For example, given the array `nums = [2,3,-2,4]`, the maximum product subarray is `[2,3]` which has a product of `6`. The function should return the maximum product of a contiguous subarray. The input array will have a length of at least 1 and at most 20000 elements, and each element will be an integer between -10^5 and 10^5.

## Approach
We will use dynamic programming to solve this problem. The idea is to maintain two variables, `maxDP` and `minDP`, which store the maximum and minimum product up to the current position. We update these variables at each step based on the current number and the previous maximum and minimum product.

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
        
        int maxDP = nums[0], minDP = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                swap(maxDP, minDP);
            }
            
            maxDP = max(nums[i], maxDP * nums[i]);
            minDP = min(nums[i], minDP * nums[i]);
            
            result = max(result, maxDP);
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
- We need to consider both the maximum and minimum product up to the current position because a negative number can turn a maximum product into a minimum product.
- We update the `maxDP` and `minDP` variables based on the current number and the previous maximum and minimum product.
- We keep track of the maximum product seen so far and return it as the result.