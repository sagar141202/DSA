# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock over time. You want to find the maximum profit that can be achieved by buying and selling the stock, with the constraint that after selling the stock, you must wait for at least one day before buying it again. The prices array will have at least one element, and all elements will be non-negative.

## Approach
The problem can be solved using dynamic programming, where we maintain three arrays: buy, sell, and cooldown. The buy array stores the maximum profit that can be achieved after buying the stock, the sell array stores the maximum profit that can be achieved after selling the stock, and the cooldown array stores the maximum profit that can be achieved after a cooldown period.

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
        
        // Initialize the buy, sell, and cooldown arrays
        vector<int> buy(n, 0);
        vector<int> sell(n, 0);
        vector<int> cooldown(n, 0);
        
        // Base case: after the first day, we can either buy the stock or not buy it
        buy[0] = -prices[0];
        
        // Fill up the arrays using dynamic programming
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum profit is the maximum of the sell and cooldown arrays at the last day
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
- We use dynamic programming to solve the problem, maintaining three arrays: buy, sell, and cooldown.
- The buy array stores the maximum profit that can be achieved after buying the stock.
- The sell array stores the maximum profit that can be achieved after selling the stock, and the cooldown array stores the maximum profit that can be achieved after a cooldown period.