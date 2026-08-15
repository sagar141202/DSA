# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in such a way that for every i, the number at position i is a multiple of i or i is a multiple of the number at position i. Given an integer n, return the number of beautiful arrangements that can be made. For example, if n = 3, the beautiful arrangements are [1, 2, 3] and [2, 1, 3] and [3, 1, 2] and [1, 3, 2] and [2, 3, 1] and [3, 2, 1], so the output should be 3.

## Approach
The problem can be solved using recursion and backtracking. We will try to place each number at each position and check if it satisfies the condition. If it does, we will recursively try to fill the rest of the positions. The algorithm will backtrack and try different placements when it finds an invalid arrangement.

## Complexity
- Time: O(n!)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countArrangement(int n) {
        vector<bool> visited(n + 1, false);
        int count = 0;
        backtrack(1, n, count, visited);
        return count;
    }

    void backtrack(int index, int n, int& count, vector<bool>& visited) {
        if (index == n + 1) {
            count++;
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && (i % index == 0 || index % i == 0)) {
                visited[i] = true;
                backtrack(index + 1, n, count, visited);
                visited[i] = false;
            }
        }
    }
};
```

## Test Cases
```
Input: n = 3
Output: 3
```

## Key Takeaways
- Use recursion and backtracking to solve the problem.
- Try to place each number at each position and check if it satisfies the condition.
- Backtrack and try different placements when an invalid arrangement is found.