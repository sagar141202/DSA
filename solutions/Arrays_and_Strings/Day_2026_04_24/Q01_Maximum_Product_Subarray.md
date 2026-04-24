# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within `nums`. A subarray is a contiguous subset of the array. The product of an empty subarray is considered to be 0. The length of `nums` is at least 1 and at most 20000. Each element in `nums` is between -10^5 and 10^5.

## Approach
To solve this problem, we can use dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product, and vice versa. We iterate through the array, updating these maximum and minimum products at each step.

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
        int maxProductSoFar = nums[0];
        int minProductSoFar = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                swap(maxProductSoFar, minProductSoFar);
            }
            
            maxProductSoFar = max(nums[i], maxProductSoFar * nums[i]);
            minProductSoFar = min(nums[i], minProductSoFar * nums[i]);
            
            result = max(result, maxProductSoFar);
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
- We must track both the maximum and minimum product up to each position because of how negative numbers can affect the product.
- The space complexity is O(1) because we only use a constant amount of space to store our variables, regardless of the size of the input array.
- This problem highlights the importance of considering edge cases, such as the presence of zero or negative numbers in the array.