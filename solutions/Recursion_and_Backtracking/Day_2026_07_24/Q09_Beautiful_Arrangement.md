# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a beautiful way, where for every i (1 <= i <= n), the number at position i is a multiple of i or i is a multiple of the number at position i. Given an integer n, return the number of beautiful arrangements that can be made. For example, if n = 3, the beautiful arrangements are [1, 2, 3] and [3, 1, 2]. If n = 4, the beautiful arrangements are [2, 4, 1, 3] and [3, 1, 4, 2].

## Approach
The problem can be solved using recursion and backtracking, where we try to place each number from 1 to n at each position and check if it satisfies the condition. We use a visited array to keep track of the numbers that have been used. The algorithm tries all possible arrangements and counts the valid ones.

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

    void backtrack(int index, int n, vector<bool>& visited, int& count) {
        if (index > n) {
            count++;
            return;
        }
        for (int i = 1; i <= n; i++) {
            if (!visited[i] && (i % index == 0 || index % i == 0)) {
                visited[i] = true;
                backtrack(index + 1, n, visited, count);
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
Input: n = 4
Output: 2
```

## Key Takeaways
- The problem requires trying all possible arrangements of numbers from 1 to n.
- The condition for a beautiful arrangement is that for every i, the number at position i is a multiple of i or i is a multiple of the number at position i.
- The solution uses recursion and backtracking to try all possible arrangements and count the valid ones.