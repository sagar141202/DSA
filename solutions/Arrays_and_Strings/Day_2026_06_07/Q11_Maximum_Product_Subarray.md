# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The array can contain both positive and negative numbers, and the maximum product can be obtained by multiplying all the numbers in the subarray. The input array will have a length of at least 1 and at most 200, and the elements will be 32-bit integers. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of `24`. However, given the array `[1, -2, -3, 0, 7, -8, -2]`, the maximum product subarray is `[7]` with a product of `7`.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can become the maximum product if multiplied by another negative number. The maximum product is updated at each step by considering the current number and the product of the current number with the previous maximum and minimum product.

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
        if (nums.size() == 0) return 0;
        
        int max_so_far = nums[0];
        int min_so_far = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                swap(max_so_far, min_so_far);
            }
            
            max_so_far = max(nums[i], max_so_far * nums[i]);
            min_so_far = min(nums[i], min_so_far * nums[i]);
            
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
- Handle the case when the current number is negative, as it can change the maximum product to minimum product and vice versa.
- Keep track of both the maximum and minimum product up to each position in the array.
- Update the result at each step by considering the current number and the product of the current number with the previous maximum product.