# Best Time to Buy and Sell Stock

## Problem Statement
Given an array of integers representing the daily stock prices, find the maximum possible profit that can be achieved by buying and selling the stock at most twice, with the constraint that you cannot sell a stock before buying it. The prices are non-negative integers, and the array has at least one element.

## Approach
We can use dynamic programming to solve this problem, keeping track of the maximum profit after the first buy, first sell, second buy, and second sell. The algorithm iterates through the array, updating these variables at each step.

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
Input: [3,3,5,0,0,3,1,4]
Output: 6
Input: [1,2,3,4,5]
Output: 4
```

## Key Takeaways
- Use dynamic programming to solve problems with overlapping subproblems and optimal substructure.
- Keep track of the maximum profit after each buy and sell to find the maximum possible profit.
- Initialize variables with negative infinity to handle cases where the maximum profit is 0.