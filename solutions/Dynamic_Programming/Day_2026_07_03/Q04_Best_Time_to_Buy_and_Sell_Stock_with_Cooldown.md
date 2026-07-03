# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the daily stock prices. The task is to find the maximum profit that can be achieved by buying and selling stocks with a cooldown period of one day. The cooldown period means that after selling a stock, you cannot buy another stock on the next day. The constraints are: you can only hold one stock at a time, and you cannot buy and sell a stock on the same day.

## Approach
The problem can be solved using dynamic programming by maintaining three arrays: buy, sell, and cooldown. The buy array stores the maximum profit after buying a stock on each day, the sell array stores the maximum profit after selling a stock on each day, and the cooldown array stores the maximum profit after a cooldown on each day.

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
        
        // Initialize arrays to store maximum profit after buying, selling, and cooldown
        vector<int> buy(n, 0), sell(n, 0), cooldown(n, 0);
        
        // Base cases
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        // Fill up the arrays using dynamic programming
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum profit is stored in the sell array
        return sell[n-1];
    }
};

int main() {
    Solution solution;
    vector<int> prices = {1, 2, 3, 0, 2};
    cout << "Maximum Profit: " << solution.maxProfit(prices) << endl;
    return 0;
}
```

## Test Cases
```
Input: prices = [1, 2, 3, 0, 2]
Output: 3
Input: prices = [1]
Output: 0
```

## Key Takeaways
- Use dynamic programming to solve problems with overlapping subproblems and optimal substructure.
- Maintain separate arrays to store the maximum profit after each state (buy, sell, cooldown) to avoid confusion and ensure correct calculations.
- Initialize base cases carefully to ensure the dynamic programming approach works correctly.