# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a way that for every i (1 <= i <= n), the number at position i is either i times a number that is already arranged, or it is a factor of i. Find the count of all such arrangements. For example, if n = 2, there are 2 arrangements: [1, 2] and [2, 1]. If n = 3, there are 3 arrangements: [1, 2, 3], [1, 3, 2], and [2, 1, 3].

## Approach
We will use recursion and backtracking to solve this problem. The algorithm will try to place each number from 1 to n at the current position, and if it satisfies the condition, it will recursively call itself to fill the remaining positions. If it doesn't satisfy the condition, it will backtrack and try the next number.

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
        backtrack(1, n, visited, count);
        return count;
    }

    void backtrack(int pos, int n, vector<bool>& visited, int& count) {
        if (pos > n) {
            count++;
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
                visited[i] = true;
                backtrack(pos + 1, n, visited, count);
                visited[i] = false;
            }
        }
    }
};
```

## Test Cases
```
Input: n = 2
Output: 2
Input: n = 3
Output: 3
```

## Key Takeaways
- Use recursion and backtracking to generate all possible arrangements.
- Use a visited array to keep track of the numbers that have been used.
- Check the condition for each number before placing it at the current position.