# Best Time to Buy and Sell Stock with Cooldown

## Problem Statement
Given an array of integers representing the prices of a stock on different days, find the maximum profit that can be achieved by buying and selling the stock with a cooldown period of one day. The cooldown period means that after selling the stock, you cannot buy it again on the next day. The problem has the following constraints: the input array will have at least one element, and all elements will be integers. For example, if the input array is [1, 2, 3, 0, 2], the maximum profit that can be achieved is 3, which is obtained by buying on the first day, selling on the third day, and then buying on the fifth day.

## Approach
The problem can be solved using dynamic programming, where we maintain three variables to track the maximum profit after the last buy, sell, and cooldown operations. We iterate through the array and update these variables based on the current price. The maximum profit is obtained by considering all possible buy and sell operations with a cooldown period.

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
        
        // Initialize variables to track the maximum profit after the last buy, sell, and cooldown operations
        vector<int> buy(n, 0), sell(n, 0), cooldown(n, 0);
        
        // Base case: the maximum profit after the first buy operation is -prices[0]
        buy[0] = -prices[0];
        
        // Iterate through the array and update the variables
        for (int i = 1; i < n; i++) {
            // The maximum profit after the current buy operation is the maximum of the previous buy operation and the previous cooldown operation minus the current price
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]);
            
            // The maximum profit after the current sell operation is the maximum of the previous sell operation and the previous buy operation plus the current price
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
            
            // The maximum profit after the current cooldown operation is the maximum of the previous cooldown operation and the previous sell operation
            cooldown[i] = max(cooldown[i-1], sell[i-1]);
        }
        
        // The maximum profit is the maximum of the last sell and cooldown operations
        return max(sell[n-1], cooldown[n-1]);
    }
};
```

## Test Cases
```
Input: prices = [1, 2, 3, 0, 2]
Output: 3
Input: prices = [1]
Output: 0
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining variables to track the maximum profit after the last buy, sell, and cooldown operations.
- The maximum profit is obtained by considering all possible buy and sell operations with a cooldown period.
- The time complexity of the solution is O(n), where n is the number of days, and the space complexity is O(n) due to the use of arrays to store the maximum profit after each operation.