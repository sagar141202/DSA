# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the daily prices of a stock. You can buy and sell the stock, but you must wait at least one day after selling before buying again. The goal is to find the maximum possible profit. The constraints are: 1 <= prices.length <= 5000, and 0 <= prices[i] <= 10^7 for all i. For example, given prices = [1, 2, 3, 0, 2], the output should be 3, which is achieved by buying at price 1, selling at price 3, and then buying at price 0 and selling at price 2.

## Approach
The problem can be solved using dynamic programming by maintaining three arrays: buy, sell, and cooldown. The buy array stores the maximum profit after buying the stock on each day, the sell array stores the maximum profit after selling the stock on each day, and the cooldown array stores the maximum profit after cooling down on each day.

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
        
        vector<int> buy(n), sell(n), cooldown(n);
        
        buy[0] = -prices[0];
        sell[0] = 0;
        cooldown[0] = 0;
        
        for (int i = 1; i < n; i++) {
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        return sell[n-1];
    }
};

int main() {
    Solution solution;
    vector<int> prices = {1, 2, 3, 0, 2};
    cout << "Maximum profit: " << solution.maxProfit(prices) << endl;
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
- The problem can be solved using dynamic programming with three arrays: buy, sell, and cooldown.
- The time complexity is O(n) where n is the number of days.
- The space complexity is O(n) for storing the buy, sell, and cooldown arrays.