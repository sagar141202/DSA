# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, and you want to arrange them in a beautiful way. A beautiful arrangement is when for every i, the number at position i is either divisible by i or i is divisible by the number at position i. Given an integer N, return the number of beautiful arrangements that can be made. For example, if N = 3, then the beautiful arrangements are [1, 2, 3], [1, 3, 2]. If N = 4, then the beautiful arrangements are [1, 2, 3, 4], [1, 3, 2, 4], [1, 2, 4, 3], [1, 4, 2, 3], [1, 4, 3, 2], [1, 3, 4, 2].

## Approach
The problem can be solved using backtracking, where we try to place each number from 1 to N at each position and check if the arrangement is beautiful. We use a helper function to check if a number can be placed at a given position. If the number is either divisible by the position or the position is divisible by the number, then we can place it.

## Complexity
- Time: O(N!)
- Space: O(N)

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
Input: N = 3
Output: 3
Input: N = 4
Output: 6
```

## Key Takeaways
- Use backtracking to try all possible arrangements of numbers.
- Use a helper function to check if a number can be placed at a given position.
- Use a visited array to keep track of the numbers that have been placed.