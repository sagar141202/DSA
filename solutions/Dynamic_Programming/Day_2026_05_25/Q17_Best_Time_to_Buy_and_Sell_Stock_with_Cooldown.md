# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
The problem is to find the maximum profit that can be achieved by buying and selling a stock with a cooldown period. The cooldown period means that after selling a stock, we cannot buy another stock for at least one day. We are given an array of stock prices where the i-th element is the price of the stock on the i-th day. The goal is to find the maximum possible profit.

## Approach
We can solve this problem using dynamic programming by maintaining three variables: buy, sell, and cooldown. The buy variable represents the maximum profit when we have a stock, the sell variable represents the maximum profit when we have sold a stock, and the cooldown variable represents the maximum profit when we are in the cooldown period.

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
        
        // initialize variables
        vector<int> buy(n, 0);
        vector<int> sell(n, 0);
        vector<int> cooldown(n, 0);
        
        // base case
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // fill up the dp tables
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // return the maximum profit
        return sell[n-1];
    }
};
```

## Test Cases
```
Input: prices = [1,2,3,0,2]
Output: 3
Input: prices = [1]
Output: 0
```

## Key Takeaways
- We can use dynamic programming to solve this problem efficiently.
- We need to maintain three variables: buy, sell, and cooldown to keep track of the maximum profit at each state.
- The final result is the maximum profit when we have sold a stock, which is stored in the sell variable.