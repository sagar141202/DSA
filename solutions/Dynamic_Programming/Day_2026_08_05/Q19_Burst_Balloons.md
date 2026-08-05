# Burst Balloons

## Problem Statement
Given n balloons, indexed from 0 to n-1. Each balloon has a certain point value. If we burst a balloon, we get points equal to the product of the two adjacent balloons (or 1 if there is no adjacent balloon). Find the maximum points we can get by bursting all the balloons.

## Approach
The algorithm uses dynamic programming to solve the problem. It builds a 2D table where each cell [i][j] represents the maximum points that can be obtained by bursting the balloons from index i to j. The final result is stored in the cell [0][n-1]. The maximum points are calculated by considering all possible balloons that can be burst first.

## Complexity
- Time: O(n^3)
- Space: O(n^2)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        vector<int> newNums = {1};
        for (int num : nums) {
            newNums.push_back(num);
        }
        newNums.push_back(1);
        n += 2;
        
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int len = 1; len <= n - 1; len++) {
            for (int left = 0; left <= n - len - 1; left++) {
                int right = left + len - 1;
                for (int i = left; i <= right; i++) {
                    dp[left][right] = max(dp[left][right], newNums[left - 1] * newNums[i] * newNums[right + 1] + (i - 1 >= left ? dp[left][i - 1] : 0) + (i + 1 <= right ? dp[i + 1][right] : 0));
                }
            }
        }
        
        return dp[1][n - 2];
    }
};
```

## Test Cases
```
Input: [3,1,5,8]
Output: 167
```

## Key Takeaways
- The problem can be solved using a dynamic programming approach with a time complexity of O(n^3).
- We need to consider all possible balloons that can be burst first to get the maximum points.
- The final result is the value stored in the cell [1][n-2] of the 2D table.