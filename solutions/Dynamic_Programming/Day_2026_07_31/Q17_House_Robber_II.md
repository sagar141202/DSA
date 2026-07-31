# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police. The street is a circle, meaning the first house is adjacent to the last house.

## Approach
The problem can be solved using dynamic programming by considering two cases: one where the first house is robbed and another where the first house is not robbed. We can then apply the standard house robber dynamic programming approach to each case.

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
        // Base case: if there are no houses, the maximum amount that can be robbed is 0
        if (nums.size() == 0) return 0;
        
        // Base case: if there is only one house, the maximum amount that can be robbed is the amount in that house
        if (nums.size() == 1) return nums[0];
        
        // Case 1: The first house is robbed
        vector<int> dp1(nums.size() - 1);
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }
        
        // Case 2: The first house is not robbed
        vector<int> dp2(nums.size() - 1);
        dp2[0] = nums[1];
        dp2[1] = max(nums[1], nums[2]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i+1]);
        }
        
        // Return the maximum amount that can be robbed in either case
        return max(dp1.back(), dp2.back());
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
- The dynamic programming approach can be used to solve problems with overlapping subproblems.
- The problem can be broken down into smaller subproblems and the solutions to these subproblems can be combined to solve the larger problem.
- The use of two separate dynamic programming arrays (dp1 and dp2) allows us to consider the two cases (where the first house is robbed and where it is not) separately.