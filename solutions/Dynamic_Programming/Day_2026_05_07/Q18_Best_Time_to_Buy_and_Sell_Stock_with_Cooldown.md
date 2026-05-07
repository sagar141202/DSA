# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day after each sale. The cooldown period means that you cannot buy the stock on the next day after selling it. For example, if the input array is [1, 2, 3, 0, 2], the maximum profit that can be achieved is 3 (buy on day 0, sell on day 2, and then buy on day 4 and sell on day 4).

## Approach
The problem can be solved using dynamic programming by maintaining three variables: buy, sell, and cooldown. The buy variable stores the maximum profit after buying the stock, the sell variable stores the maximum profit after selling the stock, and the cooldown variable stores the maximum profit after the cooldown period.

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
        if (n < 2) {
            return 0;
        }
        
        // Initialize variables
        vector<int> buy(n), sell(n), cooldown(n);
        
        // Base cases
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // Fill up the tables
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
Input: [1, 2, 3, 0, 2]
Output: 3
Input: [1]
Output: 0
```

## Key Takeaways
- Use dynamic programming to solve the problem by maintaining three variables: buy, sell, and cooldown.
- The time complexity is O(n), where n is the number of days.
- The space complexity is O(n), which can be optimized to O(1) by only keeping track of the previous day's values.