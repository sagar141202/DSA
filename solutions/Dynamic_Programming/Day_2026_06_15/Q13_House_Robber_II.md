# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob tonight without alerting the police. The street is a circle, meaning the first house is adjacent to the last house.

## Approach
The problem can be solved using dynamic programming by considering two cases: one where the first house is robbed and one where it is not. This allows us to break the circular dependency and solve the problem using a standard house robber approach. We will calculate the maximum amount that can be robbed in both cases and return the maximum of the two.

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
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return max(nums[0], nums[1]);

        // Case 1: Rob the first house
        vector<int> dp1(nums.size());
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }

        // Case 2: Do not rob the first house
        vector<int> dp2(nums.size());
        dp2[0] = 0;
        dp2[1] = nums[1];
        for (int i = 2; i < nums.size(); i++) {
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i]);
        }

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
- The problem requires breaking the circular dependency by considering two cases.
- Dynamic programming is used to solve the problem efficiently.
- The solution has a time complexity of O(n) and a space complexity of O(n), where n is the number of houses.