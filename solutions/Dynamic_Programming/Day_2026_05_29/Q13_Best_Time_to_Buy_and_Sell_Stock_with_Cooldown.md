# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array of integers representing the prices of a stock over time. You want to find the maximum profit that can be achieved by buying and selling the stock, with the condition that you cannot buy a stock on the day after you sell it (i.e., you need to have a cooldown period of one day after selling). The prices are non-negative integers, and you can only hold one stock at a time.

## Approach
We will use dynamic programming to solve this problem. The idea is to maintain three arrays: buy, sell, and cooldown, where buy[i] represents the maximum profit we can get after buying the stock on the ith day, sell[i] represents the maximum profit we can get after selling the stock on the ith day, and cooldown[i] represents the maximum profit we can get after the cooldown period on the ith day.

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
        
        return max(sell[n-1], cooldown[n-1]);
    }
};

// Example usage:
int main() {
    Solution solution;
    vector<int> prices = {1, 2, 3, 0, 2};
    cout << solution.maxProfit(prices) << endl;  // Output: 3
    return 0;
}
```

## Test Cases
```
Input: [1, 2, 3, 0, 2]
Output: 3
Input: [1]
Output: 0
Input: [1, 2]
Output: 1
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Maintain separate arrays to track the maximum profit at each step.
- Consider the cooldown period when calculating the maximum profit after selling the stock.