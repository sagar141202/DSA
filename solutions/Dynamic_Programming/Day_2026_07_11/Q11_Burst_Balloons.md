# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain amount of coins associated with it, and when a balloon is burst, all the coins from the previous balloons that are still intact are added to the total coins. The goal is to find the maximum amount of coins that can be collected by bursting the balloons in a specific order. The balloons are initially arranged in a line, and when a balloon is burst, the adjacent balloons are moved closer to fill the gap. The problem has the following constraints: 1 <= n <= 500, and the amount of coins associated with each balloon is a positive integer.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the maximum coins that can be collected by bursting the balloons in a specific range. We then fill up the table in a bottom-up manner, considering all possible orders of bursting the balloons. The key insight is to consider the last balloon to be burst in each range.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        // add dummy balloons with 1 coin at the beginning and end
        vector<int> newNums = {1};
        for (int num : nums) {
            newNums.push_back(num);
        }
        newNums.push_back(1);
        
        // build a 2D table to store the maximum coins
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        // fill up the table in a bottom-up manner
        for (int length = 1; length <= n + 1; length++) {
            for (int left = 0; left <= n + 1 - length; left++) {
                int right = left + length - 1;
                for (int i = left; i <= right; i++) {
                    // consider the current balloon as the last one to be burst
                    int coins = newNums[left - 1] * newNums[i] * newNums[right + 1];
                    if (i > left) {
                        coins += dp[left][i - 1];
                    }
                    if (i < right) {
                        coins += dp[i + 1][right];
                    }
                    // update the maximum coins
                    dp[left][right] = max(dp[left][right], coins);
                }
            }
        }
        
        // return the maximum coins
        return dp[1][n];
    }
};

int main() {
    Solution solution;
    vector<int> nums = {3, 1, 5, 8};
    cout << solution.maxCoins(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [3, 1, 5, 8]
Output: 167
```

## Key Takeaways
- The problem can be solved using dynamic programming, where we build a 2D table to store the maximum coins that can be collected by bursting the balloons in a specific range.
- The time complexity is O(n^3), where n is the number of balloons, due to the three nested loops.
- The space complexity is O(n^2), where n is the number of balloons, due to the 2D table used to store the maximum coins.