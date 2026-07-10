# House Robber II

## Problem Statement
The problem "House Robber II" involves finding the maximum amount of money that can be stolen from a list of houses, with the constraint that no two adjacent houses can be robbed. The houses are arranged in a circle, meaning that the first house is adjacent to the last house. The input is a list of integers representing the amount of money in each house, and the output is the maximum amount of money that can be stolen. For example, given the input [2,3,2], the output would be 3, because the maximum amount of money that can be stolen is 3, which is the amount of money in the second house.

## Approach
The algorithm uses dynamic programming to solve the problem by considering two cases: one where the first house is robbed and one where the first house is not robbed. The maximum amount of money that can be stolen in each case is calculated separately, and the maximum of the two cases is returned as the final answer. This approach ensures that the constraint of not robbing adjacent houses is satisfied.

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
Input: [2,3,2]
Output: 3
Input: [1,2,3,1]
Output: 4
Input: [1,2,3]
Output: 3
```

## Key Takeaways
- The problem can be solved using dynamic programming by considering two cases: one where the first house is robbed and one where the first house is not robbed.
- The maximum amount of money that can be stolen in each case is calculated separately, and the maximum of the two cases is returned as the final answer.
- The time complexity of the solution is O(n), where n is the number of houses, and the space complexity is also O(n).