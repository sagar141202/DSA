# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the daily prices of a stock. The goal is to find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day after each sale. The constraints are that you can only hold one stock at a time and you cannot buy and sell on the same day. For example, if the input is [1, 2, 3, 0, 2], the output should be 3, which is achieved by buying on day 0, selling on day 2, and then buying on day 4 and selling on day 4.

## Approach
The problem can be solved using dynamic programming by maintaining three arrays: buy, sell, and cooldown. The buy array stores the maximum profit after buying the stock on each day, the sell array stores the maximum profit after selling the stock on each day, and the cooldown array stores the maximum profit after the cooldown period on each day.

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
        
        // Initialize buy, sell, and cooldown arrays
        vector<int> buy(n), sell(n), cooldown(n);
        
        // Base case: buy on day 0
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // Fill up the arrays using dynamic programming
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum profit is stored in the sell array on the last day
        return sell[n-1];
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 0, 2]
Output: 3
Input: [1]
Output: 0
```

## Key Takeaways
- The problem can be broken down into three states: buying, selling, and cooldown.
- Dynamic programming is used to fill up the arrays and find the maximum profit.
- The maximum profit is stored in the sell array on the last day.