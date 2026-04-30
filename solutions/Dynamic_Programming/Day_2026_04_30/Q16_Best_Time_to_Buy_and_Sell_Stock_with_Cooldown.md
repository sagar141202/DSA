# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
The problem requires finding the maximum profit that can be achieved by buying and selling a stock with a cooldown period. The cooldown period means that after selling a stock, we cannot buy another stock on the next day. We are given an array of prices where prices[i] is the price of the stock on the ith day. The goal is to find the maximum possible profit.

## Approach
The approach involves using dynamic programming to track the maximum profit at each day. We use three variables: buy, sell, and cooldown, to represent the maximum profit when we have bought the stock, sold the stock, and are in the cooldown period, respectively.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        
        // Initialize variables to store the maximum profit
        vector<int> buy(n), sell(n), cooldown(n);
        
        // Base cases
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // Fill up the dp arrays
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum profit is the maximum of sell and cooldown on the last day
        return max(sell[n-1], cooldown[n-1]);
    }
};
```

## Test Cases
```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: Buy on day 1, sell on day 3, and then buy on day 4 and sell on day 5.

Input: prices = [1]
Output: 0
Explanation: No profit can be achieved.
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize base cases carefully to ensure the correctness of the solution.
- Use meaningful variable names to improve the readability of the code.