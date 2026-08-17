# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police. The street is a circle, meaning the first house is adjacent to the last house.

## Approach
The algorithm uses dynamic programming to track the maximum amount that can be robbed up to each house. It considers two cases: robbing the first house and not robbing the first house. The maximum of these two cases is the final answer.

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
        // case 1: rob the first house
        int max1 = helper(nums, 0, nums.size() - 2);
        // case 2: do not rob the first house
        int max2 = helper(nums, 1, nums.size() - 1);
        return max(max1, max2);
    }
    
    int helper(vector<int>& nums, int start, int end) {
        int prev = 0, curr = 0;
        for (int i = start; i <= end; i++) {
            int temp = curr;
            curr = max(curr, prev + nums[i]);
            prev = temp;
        }
        return curr;
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
- The problem can be divided into two subproblems: robbing the first house and not robbing the first house.
- Dynamic programming is used to solve each subproblem efficiently.
- The final answer is the maximum of the two subproblems.