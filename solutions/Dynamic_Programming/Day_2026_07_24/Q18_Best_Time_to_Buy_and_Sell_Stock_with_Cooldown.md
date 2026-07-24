# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock over time. You can buy and sell the stock, but you must wait at least one day after selling before buying again. The goal is to find the maximum profit that can be achieved. The constraints are: 1 <= prices.length <= 5000, and 0 <= prices[i] <= 10^7. For example, if the input is [1, 2, 3, 0, 2], the output should be 3, which is achieved by buying at price 1, selling at price 3, and then buying at price 0 and selling at price 2.

## Approach
The algorithm uses dynamic programming to track the maximum profit at each time step, considering the cooldown period after selling. It maintains three variables: buy, sell, and cooldown, representing the maximum profit when the last action was a buy, sell, or cooldown, respectively.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        
        // Initialize variables to store maximum profit
        vector<int> buy(n), sell(n), cooldown(n);
        
        // Base cases
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // Fill up the dp tables
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // Return the maximum profit
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
- The dynamic programming approach helps to avoid redundant calculations and improves efficiency.
- The use of three variables (buy, sell, cooldown) allows us to track the maximum profit at each time step, considering the cooldown period after selling.
- The base cases are crucial to initialize the dp tables correctly, ensuring that the algorithm produces the correct output.