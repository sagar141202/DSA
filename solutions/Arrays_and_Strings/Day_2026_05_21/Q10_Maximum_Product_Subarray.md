# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The array can contain both positive and negative numbers. The maximum product subarray must be a contiguous subarray, and the product of all elements in the subarray must be calculated. For example, given the array `[-2, 3, -4]`, the maximum product subarray is `[-2, 3, -4]` with a product of `24`. The array can be empty, and the length of the array is at most `200`. All elements in the array are integers between `-10^5` and `10^5`.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product. The maximum product at each position is updated based on the maximum and minimum product at the previous position.

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
- The algorithm has a time complexity of O(n), where n is the length of the input array.
- The algorithm uses a constant amount of space to store the maximum and minimum product up to each position.
- The algorithm handles negative numbers by swapping the maximum and minimum product when a negative number is encountered.