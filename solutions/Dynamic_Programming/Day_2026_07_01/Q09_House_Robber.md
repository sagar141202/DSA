# House Robber

## Problem Statement
The House Robber problem is a classic dynamic programming problem where you are given a list of non-negative integers representing the amount of money in each house. The goal is to find the maximum amount of money that can be stolen from the houses without stealing from adjacent houses. The problem has the following constraints: there are at least one and at most 100 houses, and each house contains between 0 and 400 dollars.

## Approach
The algorithm uses dynamic programming to solve the problem by maintaining two variables: one for the maximum amount of money that can be stolen up to the current house, and another for the maximum amount of money that can be stolen up to the previous house. The maximum amount of money that can be stolen from the current house is the maximum of the money that can be stolen from the previous house and the money that can be stolen from the house two positions before plus the money in the current house.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        if (nums.size() == 1) return nums[0];
        
        // Initialize dp array
        vector<int> dp(nums.size());
        
        // Base cases
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        // Fill up dp array
        for (int i = 2; i < nums.size(); i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        return dp[nums.size() - 1];
    }
};
```

## Test Cases
```
Input: [1,2,3,1]
Output: 4
Input: [2,7,9,3,1]
Output: 12
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- The House Robber problem is an example of a 1D dynamic programming problem, where we need to maintain a table of solutions to subproblems.
- The time complexity of the solution is linear, and the space complexity can be optimized to O(1) by only keeping track of the last two houses.