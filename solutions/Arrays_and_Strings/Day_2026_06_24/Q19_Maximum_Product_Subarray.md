# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The array can contain both positive and negative numbers, and the product of an empty subarray is considered to be 0. The maximum product subarray is the subarray with the largest product. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3]` with a product of 6, but for the array `[0,2]`, the maximum product subarray is `[2]` with a product of 2.

## Approach
The algorithm involves iterating over the array and at each step, considering the maximum product that can be obtained by including the current element. This is done by keeping track of the maximum and minimum product up to the current element. The maximum product is updated if the current product (obtained by multiplying the current element with the previous maximum product) is greater than the current element itself or the previous minimum product multiplied by the current element.

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
        
        int max_so_far = nums[0];
        int min_so_far = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            int temp = max_so_far;
            max_so_far = max(nums[i], max(max_so_far * nums[i], min_so_far * nums[i]));
            min_so_far = min(nums[i], min(temp * nums[i], min_so_far * nums[i]));
            result = max(result, max_so_far);
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
- The solution involves maintaining two variables, `max_so_far` and `min_so_far`, to keep track of the maximum and minimum product up to the current element.
- At each step, the maximum product is updated by considering the product of the current element with the previous maximum and minimum products.
- The use of `temp` variable is to avoid overwriting the value of `max_so_far` before it's used to update `min_so_far`.