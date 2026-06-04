# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
The problem is to find the maximum profit that can be achieved by buying and selling a stock with a cooldown period. The cooldown period means that after selling a stock, we cannot buy another stock for a certain number of days. We are given an array of integers representing the prices of the stock on different days. The goal is to find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of 1 day. For example, if the prices are [1, 2, 3, 0, 2], the maximum profit is 3, which can be achieved by buying on day 0, selling on day 2, and then buying on day 4 and selling on day 4.

## Approach
The approach is to use dynamic programming to keep track of the maximum profit that can be achieved at each day. We will maintain three variables: buy, sell, and cooldown, which represent the maximum profit that can be achieved by buying, selling, and cooling down on the current day, respectively. The transition between these states will be based on the maximum profit that can be achieved by either buying, selling, or cooling down on the previous day.

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
        
        // Initialize variables to store the maximum profit at each day
        vector<int> buy(n), sell(n), cooldown(n);
        
        // Base case: the maximum profit on the first day is -prices[0] if we buy the stock
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // Fill up the dp table
        for (int i = 1; i < n; i++) {
            // The maximum profit if we buy the stock on the current day is the maximum of the profit if we buy the stock on the previous day and the profit if we cooldown on the previous day minus the price of the stock on the current day
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            // The maximum profit if we sell the stock on the current day is the maximum of the profit if we sell the stock on the previous day and the profit if we buy the stock on the previous day plus the price of the stock on the current day
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            // The maximum profit if we cooldown on the current day is the maximum of the profit if we cooldown on the previous day and the profit if we sell the stock on the previous day
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum profit is the maximum of the profit if we sell the stock on the last day and the profit if we cooldown on the last day
        return max(sell[n-1], cooldown[n-1]);
    }
};
```

## Test Cases
```
Input: prices = [1, 2, 3, 0, 2]
Output: 3
Input: prices = [1]
Output: 0
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining three variables: buy, sell, and cooldown, which represent the maximum profit that can be achieved by buying, selling, and cooling down on the current day, respectively.
- The transition between these states is based on the maximum profit that can be achieved by either buying, selling, or cooling down on the previous day.
- The time complexity of the solution is O(n), where n is the number of days, and the space complexity is also O(n).