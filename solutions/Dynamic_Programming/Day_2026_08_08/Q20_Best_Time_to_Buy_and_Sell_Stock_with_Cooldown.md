# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day. The cooldown period means that after selling the stock, we cannot buy it again on the next day. The constraints are that we can only hold one stock at a time, and we must sell the stock before buying it again. For example, if the input array is [1, 2, 3, 0, 2], the maximum profit is 3, which can be achieved by buying on the first day, selling on the third day, and then buying and selling on the last two days.

## Approach
We can solve this problem using dynamic programming by maintaining three arrays: buy, sell, and cool. The buy array stores the maximum profit after buying the stock on each day, the sell array stores the maximum profit after selling the stock on each day, and the cool array stores the maximum profit after cooling down on each day.

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
        
        // Initialize the buy, sell, and cool arrays
        vector<int> buy(n, 0);
        vector<int> sell(n, 0);
        vector<int> cool(n, 0);
        
        // Initialize the base cases
        buy[0] = -prices[0];
        sell[0] = 0;
        cool[0] = 0;
        
        // Fill up the buy, sell, and cool arrays
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cool[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cool[i] = max(cool[i-1], sell[i-1]);
        }
        
        // The maximum profit is stored in the last element of the sell array
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
- We need to maintain three separate arrays to keep track of the maximum profit after buying, selling, and cooling down on each day.
- The base cases for the buy, sell, and cool arrays need to be initialized carefully to ensure that the dynamic programming approach works correctly.
- The maximum profit is stored in the last element of the sell array, which represents the maximum profit that can be achieved after selling the stock on the last day.