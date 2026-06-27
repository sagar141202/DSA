# Paint House

## Problem Statement
There are a row of houses, each house can be painted with three colors: red, blue and green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. The cost of painting each house with a certain color is given. You need to find the minimum cost to paint all houses.

## Approach
The algorithm uses dynamic programming to build up a solution by considering each house one by one. It maintains the minimum cost of painting the current house with each color, based on the minimum cost of painting the previous house with the other two colors. This approach ensures that no two adjacent houses have the same color.

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
        // base case: only one house
        if (n == 1) return min({costs[0][0], costs[0][1], costs[0][2]});
        
        // initialize the dp array with the cost of the first house
        int prevRed = costs[0][0];
        int prevBlue = costs[0][1];
        int prevGreen = costs[0][2];
        
        for (int i = 1; i < n; i++) {
            int currRed = costs[i][0] + min(prevBlue, prevGreen);
            int currBlue = costs[i][1] + min(prevRed, prevGreen);
            int currGreen = costs[i][2] + min(prevRed, prevBlue);
            // update the dp array for the next house
            prevRed = currRed;
            prevBlue = currBlue;
            prevGreen = currGreen;
        }
        
        // the minimum cost is the minimum of the costs of the last house with each color
        return min({prevRed, prevBlue, prevGreen});
    }
};
```

## Test Cases
```
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Consider each house one by one and maintain the minimum cost of painting the current house with each color.
- The minimum cost to paint all houses is the minimum of the costs of the last house with each color.