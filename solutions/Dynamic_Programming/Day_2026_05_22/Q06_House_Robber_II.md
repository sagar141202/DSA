# House Robber II

## Problem Statement
You are a professional thief planning to rob houses along a street. Each house has a certain amount of money stashed. All houses in this place are arranged in a circle, meaning the first house is connected to the last one. You cannot rob adjacent houses. Given a list of non-negative integers representing the amount of money in each house, determine the maximum amount of money you can rob.

## Approach
The algorithm uses dynamic programming to solve two separate instances of the House Robber problem, excluding the first and last house respectively. It then returns the maximum of these two instances. The intuition is to break the circle into two separate lines and apply the standard House Robber solution.

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
        // Base cases
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];

        // Rob the circle excluding the first house
        vector<int> dp1(nums.size() - 1);
        dp1[0] = nums[1];
        dp1[1] = max(nums[1], nums[2]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i+1]);
        }

        // Rob the circle excluding the last house
        vector<int> dp2(nums.size() - 1);
        dp2[0] = nums[0];
        dp2[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.size() - 1; i++) {
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i]);
        }

        // Return the maximum of the two instances
        return max(dp1.back(), dp2.back());
    }
};
```

## Test Cases
```
Input: [2,3,2]
Output: 3
Input: [1,2,3,1]
Output: 4
Input: [0]
Output: 0
```

## Key Takeaways
- Break down complex problems into simpler sub-problems.
- Use dynamic programming to store and reuse the solutions to sub-problems.
- Consider the base cases and edge cases when implementing the solution.