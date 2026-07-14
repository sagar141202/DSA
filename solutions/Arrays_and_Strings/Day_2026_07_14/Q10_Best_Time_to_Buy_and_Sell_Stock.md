# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock at most twice, with the constraint that you must sell the stock before buying it again. The input array will contain at least one element, and all elements will be positive integers.

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
        
        // Iterate through the array of prices
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
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Input: prices = [1,2,3,4,5]
Output: 4
```

## Key Takeaways
- The algorithm uses dynamic programming to track the maximum profit at each step.
- The time complexity is O(n), where n is the number of days (i.e., the length of the input array).
- The space complexity is O(1), as the algorithm only uses a constant amount of space to store the maximum profit variables.