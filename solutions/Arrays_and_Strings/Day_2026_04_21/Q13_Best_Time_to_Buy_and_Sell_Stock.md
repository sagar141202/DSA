# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock at most twice, with the constraint that the second buy must be made after the first sell. The prices array has at least one element, and all elements are non-negative.

## Approach
The algorithm uses dynamic programming to track the maximum profit after the first buy, first sell, second buy, and second sell. It iterates over the prices array, updating these variables at each step. The maximum possible profit is the maximum profit after the second sell.

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
        int buy1 = INT_MIN, sell1 = 0, buy2 = INT_MIN, sell2 = 0;
        for (int price : prices) {
            buy1 = max(buy1, -price);
            sell1 = max(sell1, buy1 + price);
            buy2 = max(buy2, sell1 - price);
            sell2 = max(sell2, buy2 + price);
        }
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
- The maximum profit after the first buy is the maximum of the current maximum and the negative of the current price.
- The maximum profit after the second buy is the maximum of the current maximum and the maximum profit after the first sell minus the current price.
- Dynamic programming can be used to solve problems with overlapping subproblems and optimal substructure.