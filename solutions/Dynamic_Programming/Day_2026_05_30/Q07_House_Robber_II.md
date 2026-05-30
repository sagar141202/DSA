# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed. All houses are arranged in a circle, meaning the first house is connected to the last one. You cannot rob adjacent houses. Given an array of integers representing the amount of money in each house, return the maximum amount of money you can rob. Constraints: 1 <= nums.length <= 10^4, 0 <= nums[i] <= 10^4. Example: Input: nums = [2,3,2], Output: 3.

## Approach
This problem can be solved using dynamic programming by breaking it down into two sub-problems: one where the first house is robbed and one where it is not. We then find the maximum amount that can be robbed in each case. 

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        // Base case: if there are no houses, return 0
        if (nums.size() == 0) return 0;
        // Base case: if there is only one house, return the money in that house
        if (nums.size() == 1) return nums[0];
        // Base case: if there are only two houses, return the maximum money
        if (nums.size() == 2) return max(nums[0], nums[1]);
        
        // Calculate the maximum money if the first house is robbed
        vector<int> dp1(nums.size());
        dp1[0] = nums[0];
        dp1[1] = nums[0];
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }
        
        // Calculate the maximum money if the first house is not robbed
        vector<int> dp2(nums.size());
        dp2[0] = 0;
        dp2[1] = nums[1];
        for (int i = 2; i < nums.size(); i++) {
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i]);
        }
        
        // Return the maximum money
        return max(dp1[nums.size() - 2], dp2[nums.size() - 1]);
    }
};
```

## Test Cases
```
Input: nums = [2,3,2]
Output: 3
Input: nums = [1,2,3,1]
Output: 4
Input: nums = [0]
Output: 0
```

## Key Takeaways
- To solve this problem, we use dynamic programming to calculate the maximum amount of money that can be robbed in two cases: when the first house is robbed and when it is not.
- We use two arrays, dp1 and dp2, to store the maximum amount of money that can be robbed up to each house in the two cases.
- The final answer is the maximum of the maximum amounts in the two cases.