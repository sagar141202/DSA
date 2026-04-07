# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is given. You need to find the minimum cost to paint all the houses.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell represents the minimum cost to paint the houses up to that point with a specific color. The minimum cost to paint a house with a certain color is the minimum cost to paint the previous house with a different color plus the cost to paint the current house with the current color.

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
        
        // base case
        dp[0][0] = costs[0][0];
        dp[0][1] = costs[0][1];
        dp[0][2] = costs[0][2];
        
        for (int i = 1; i < n; i++) {
            dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2]);
            dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2]);
            dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1]);
        }
        
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
- Use dynamic programming to solve the problem by maintaining a 2D array to store the minimum cost to paint the houses up to each point with a specific color.
- The time complexity is O(n) where n is the number of houses.
- The space complexity is O(n) where n is the number of houses.