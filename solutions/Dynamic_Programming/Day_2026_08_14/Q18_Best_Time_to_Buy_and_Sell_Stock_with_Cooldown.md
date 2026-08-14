# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You want to maximize your profit by buying and selling the stock with a cooldown period of one day after each sell. The cooldown period means that after you sell the stock, you cannot buy the stock again until one day has passed. Find the maximum possible profit.

## Approach
The problem can be solved using dynamic programming by maintaining three variables: `buy`, `sell`, and `cooldown`, representing the maximum profit after buying, selling, and cooling down respectively. We update these variables iteratively based on the current price.

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
        
        // base case
        vector<int> buy(n), sell(n), cooldown(n);
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        for (int i = 1; i < n; i++) {
            // update buy
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            // update sell
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            // update cooldown
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        return max(sell[n-1], cooldown[n-1]);
    }
};
```

## Test Cases
```
Input: prices = [1,2,3,0,2]
Output: 3
```

## Key Takeaways
- We use dynamic programming to solve this problem efficiently.
- The `buy`, `sell`, and `cooldown` arrays help us keep track of the maximum profit at each step.
- The final answer is the maximum of `sell[n-1]` and `cooldown[n-1]`, representing the maximum possible profit after selling or cooling down on the last day.