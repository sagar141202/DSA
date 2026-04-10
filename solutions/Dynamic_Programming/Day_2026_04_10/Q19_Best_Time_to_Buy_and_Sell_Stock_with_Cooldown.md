# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You want to maximize your profit by buying and selling the stock with a cooldown period of one day after each sale. The cooldown period means that after selling the stock on the `i-th` day, you cannot buy the stock again until the `(i+2)-th` day. Find the maximum possible profit.

## Approach
The problem can be solved using dynamic programming by maintaining three states: buy, sell, and cooldown. We iterate through the prices array, updating these states at each step. The maximum profit is the maximum value of the sell state at the end.

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
        
        // Initialize dp array with -1
        vector<vector<int>> dp(n, vector<int>(3, -1));
        
        // Function to calculate max profit
        function<int(int, int)> calculateMaxProfit = 
            [&] (int index, int state) {
                if (index >= n) {
                    if (state == 0) return INT_MIN; // cannot buy after last day
                    return 0;
                }
                if (dp[index][state] != -1) return dp[index][state];
                
                int profit = 0;
                if (state == 0) { // buy state
                    profit = max(0 + calculateMaxProfit(index + 1, 0), 
                                 -prices[index] + calculateMaxProfit(index + 1, 1));
                } else if (state == 1) { // sell state
                    profit = max(0 + calculateMaxProfit(index + 1, 1), 
                                 prices[index] + calculateMaxProfit(index + 1, 2));
                } else { // cooldown state
                    profit = 0 + calculateMaxProfit(index + 1, 0);
                }
                
                dp[index][state] = profit;
                return profit;
            };
        
        return calculateMaxProfit(0, 0);
    }
};
```

## Test Cases
```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: 
- Buy on day 1 and sell on day 3, then buy on day 5. 
Total profit is 2 + 1 = 3.
```

## Key Takeaways
- We use dynamic programming to solve this problem efficiently by avoiding redundant calculations.
- The problem can be divided into three states: buy, sell, and cooldown, which helps us to break down the problem into smaller subproblems.
- The time complexity is O(n) and the space complexity is O(n), where n is the number of days.