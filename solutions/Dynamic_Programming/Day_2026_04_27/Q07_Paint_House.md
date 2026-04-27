# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color, and you need to find the minimum cost to paint all the houses. The cost of painting each house with each color is given in a 2D array, where costs[i][0], costs[i][1], costs[i][2] are the costs of painting the i-th house with red, blue, and green respectively.

## Approach
We will use dynamic programming to solve this problem, by maintaining the minimum cost of painting the current house with each color. We will consider the minimum cost of painting the previous house with the other two colors.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        if (costs.empty()) return 0;
        int n = costs.size();
        int red = costs[0][0], blue = costs[0][1], green = costs[0][2];
        for (int i = 1; i < n; i++) {
            int newRed = min(blue, green) + costs[i][0];
            int newBlue = min(red, green) + costs[i][1];
            int newGreen = min(red, blue) + costs[i][2];
            red = newRed;
            blue = newBlue;
            green = newGreen;
        }
        return min(min(red, blue), green);
    }
};
```

## Test Cases
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
```

## Key Takeaways
- We only need to keep track of the minimum cost of painting the current house with each color.
- The minimum cost of painting the current house with a certain color is the minimum cost of painting the previous house with the other two colors, plus the cost of painting the current house with the current color.
- We can solve this problem in O(n) time complexity, where n is the number of houses.