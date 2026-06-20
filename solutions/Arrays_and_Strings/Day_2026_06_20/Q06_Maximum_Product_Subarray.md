# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a contiguous subarray within the array. The array can contain both positive and negative integers. The maximum product subarray is the subarray with the largest product of its elements. For example, given the array `[-2, 3, -4]`, the maximum product subarray is `[-2, 3, -4]` with a product of `24`. The array can be empty, and the maximum product of an empty array is `0`. The input array will have at most `200` elements, and each element will be in the range `[-10^5, 10^5]`.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product of subarrays ending at each position. This is necessary because a negative number can turn a maximum product into a minimum product. The maximum product of a subarray ending at the current position is the maximum of the current number, the product of the current number and the maximum product of the subarray ending at the previous position, and the product of the current number and the minimum product of the subarray ending at the previous position.

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
Input: nums = [0,2]
Output: 2
```

## Key Takeaways
- The maximum product subarray can start and end at any position in the array.
- A negative number can turn a maximum product into a minimum product, so we need to track both the maximum and minimum product of subarrays ending at each position.
- The time complexity is O(n), where n is the number of elements in the array, because we only need to iterate through the array once.