# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock at most twice. The constraint is that you cannot buy the stock before selling it, and you cannot sell the stock before buying it. For example, if the input array is [3, 3, 5, 0, 0, 3, 1, 4], the maximum possible profit is 6, which can be achieved by buying the stock at price 3, selling it at price 5, buying it again at price 0, and selling it at price 4.

## Approach
The algorithm uses dynamic programming to track the maximum profit after the first buy, first sell, second buy, and second sell. It iterates through the array, updating these values based on the current price. The maximum possible profit is the maximum value after the second sell.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Initialize variables to store the maximum profit after the first buy, first sell, second buy, and second sell
        int first_buy = INT_MIN, first_sell = 0, second_buy = INT_MIN, second_sell = 0;
        
        // Iterate through the array of prices
        for (int price : prices) {
            // Update the maximum profit after the first buy
            first_buy = max(first_buy, -price);
            // Update the maximum profit after the first sell
            first_sell = max(first_sell, first_buy + price);
            // Update the maximum profit after the second buy
            second_buy = max(second_buy, first_sell - price);
            // Update the maximum profit after the second sell
            second_sell = max(second_sell, second_buy + price);
        }
        
        // Return the maximum possible profit
        return second_sell;
    }
};
```

## Test Cases
```
Input: [3, 3, 5, 0, 0, 3, 1, 4]
Output: 6
Input: [1, 2, 3, 4, 5]
Output: 4
Input: [7, 6, 4, 3, 1]
Output: 0
```

## Key Takeaways
- The algorithm uses dynamic programming to track the maximum profit after each transaction.
- The time complexity is O(n), where n is the number of days, and the space complexity is O(1), as it only uses a constant amount of space.
- The algorithm can be extended to handle more than two transactions by adding more variables to track the maximum profit after each transaction.