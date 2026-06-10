# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array `nums` representing the amount of money in each house, return the maximum amount of money you can rob. The street is a circle, meaning the first house is adjacent to the last house, so you cannot rob the first and last house at the same time.

## Approach
The problem can be solved using dynamic programming by considering two cases: one where the first house is robbed and one where it is not. The maximum amount of money that can be robbed in each case is calculated separately. The algorithm iterates through the array, at each step deciding whether to rob the current house or not, based on the maximum amount of money that can be robbed up to the previous house.

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
        
        // case 1: rob the first house
        vector<int> dp1(nums.size());
        dp1[0] = nums[0];
        dp1[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i]);
        }
        
        // case 2: do not rob the first house
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
- The problem is a variation of the classic "House Robber" problem, with the added constraint of the street being a circle.
- Dynamic programming is used to solve the problem, with two separate cases considered: one where the first house is robbed and one where it is not.
- The time complexity is O(n), where n is the number of houses, and the space complexity is also O(n) due to the use of two arrays to store the maximum amount of money that can be robbed up to each house.