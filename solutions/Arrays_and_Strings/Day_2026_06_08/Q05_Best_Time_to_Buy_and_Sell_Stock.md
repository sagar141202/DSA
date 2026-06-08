# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock at most twice. The stock can only be sold after it is bought, and the same stock cannot be bought and sold on the same day. The input array will have at least one element, and all elements will be non-negative integers. For example, if the input array is [3, 3, 5, 0, 0, 3, 1, 4], the maximum possible profit is 6, which can be achieved by buying at price 3, selling at price 5, buying at price 0, and selling at price 4.

## Approach
The algorithm uses dynamic programming to track the maximum profit after the first buy, first sell, second buy, and second sell. It iterates through the array, updating these values based on the current price. The maximum possible profit is the maximum profit after the second sell.

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
        // Initialize variables to track the maximum profit
        int buy1 = INT_MIN, sell1 = 0, buy2 = INT_MIN, sell2 = 0;
        
        // Iterate through the array
        for (int price : prices) {
            // Update the maximum profit after the first buy
            buy1 = max(buy1, -price);
            // Update the maximum profit after the first sell
            sell1 = max(sell1, buy1 + price);
            // Update the maximum profit after the second buy
            buy2 = max(buy2, sell1 - price);
            // Update the maximum profit after the second sell
            sell2 = max(sell2, buy2 + price);
        }
        
        // Return the maximum possible profit
        return sell2;
    }
};
```

## Test Cases
```
Input: [3, 3, 5, 0, 0, 3, 1, 4]
Output: 6
Input: [1, 2, 3, 4, 5]
Output: 4
```

## Key Takeaways
- The algorithm uses dynamic programming to track the maximum profit after each buy and sell.
- The maximum possible profit is the maximum profit after the second sell.
- The time complexity is O(n), where n is the number of days, and the space complexity is O(1), as only a constant amount of space is used.