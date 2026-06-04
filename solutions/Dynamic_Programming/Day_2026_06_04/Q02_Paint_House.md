# Paint House

## Problem Statement
There are a row of houses, each house can be painted with one of the three colors: red, blue, and green. The cost of painting each house with a particular color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a particular color is given. Find the minimum cost to paint all the houses.

## Approach
We will use dynamic programming to build up a solution. We'll maintain three arrays, one for each color, where the ith element in each array represents the minimum cost to paint the first i houses with the last house being the corresponding color. We'll fill up these arrays iteratively, considering the minimum cost of painting the previous house with a different color.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty()) return 0;
        
        int n = costs.size();
        vector<vector<int>> dp(n, vector<int>(3, 0));
        
        // Initialize the base case
        dp[0][0] = costs[0][0];
        dp[0][1] = costs[0][1];
        dp[0][2] = costs[0][2];
        
        // Fill up the dp array
        for (int i = 1; i < n; i++) {
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2]);
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2]);
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1]);
        }
        
        // The minimum cost is the minimum of the last row
        return min({dp[n-1][0], dp[n-1][1], dp[n-1][2]});
    }
};
```

## Test Cases
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Consider all possible cases and choose the one that gives the minimum cost.
- The time complexity can be reduced by only keeping track of the previous row in the dp array.