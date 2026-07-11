# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day. The cooldown period means that after selling the stock, you cannot buy it again on the next day. The constraints are: you can only hold one stock at a time, and you must sell the stock before buying it again.

## Approach
The algorithm uses dynamic programming to track the maximum profit at each day. It maintains three variables: buy, sell, and cooldown, representing the maximum profit when holding the stock, when not holding the stock after selling, and when in the cooldown period, respectively.

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
        
        // The maximum profit is stored in the sell array
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
- Use dynamic programming to solve problems with overlapping subproblems.
- The cooldown period adds an extra layer of complexity, requiring the use of an additional variable to track the maximum profit during the cooldown period.
- The base cases are crucial in dynamic programming, as they provide the foundation for the recursive or iterative solution.