# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
Given an array of integers representing the prices of a stock over time, find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day after each sale. The cooldown period means that after selling the stock, you cannot buy it again until one day has passed. The goal is to maximize the total profit.

## Approach
The problem can be solved using dynamic programming by maintaining three arrays: buy, sell, and cool. The buy array stores the maximum profit after buying the stock, the sell array stores the maximum profit after selling the stock, and the cool array stores the maximum profit after the cooldown period.

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
        
        vector<int> buy(n), sell(n), cool(n);
        buy[0] = -prices[0];
        sell[0] = 0;
        cool[0] = 0;
        
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cool[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cool[i] = max(cool[i-1], sell[i-1]);
        }
        
        return sell[n-1];
    }
};
```

## Test Cases
```
Input: prices = [1, 2, 3, 0, 2]
Output: 3
Explanation: Buy on day 1 (price=1) and sell on day 3 (price=3), then buy on day 5 (price=0) and sell on day 5 (price=2).
```

## Key Takeaways
- Use dynamic programming to maintain the maximum profit at each step.
- The buy, sell, and cool arrays help to keep track of the maximum profit after buying, selling, and cooling down, respectively.
- The final result is stored in the sell array at the last index.