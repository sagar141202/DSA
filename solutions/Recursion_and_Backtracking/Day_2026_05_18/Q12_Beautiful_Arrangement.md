# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a way that for every i (1 <= i <= n), the number at position i is either i times a number that comes after it or it is a factor of a number that comes after it. The task is to find the number of possible arrangements. For example, if n = 2, there is only one possible arrangement: [1, 2]. If n = 3, there are 3 possible arrangements: [1, 2, 3], [2, 1, 3], [2, 3, 1].

## Approach
The problem can be solved using recursion and backtracking. We can start by placing the number 1 at the first position and then try to place the remaining numbers one by one, making sure that the condition is satisfied at each step. If we cannot place a number, we backtrack and try a different arrangement.

## Complexity
- Time: O(k) where k is the number of possible arrangements
- Space: O(n) for the recursion stack

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
Input: n = 2
Output: 1
Input: n = 3
Output: 3
```

## Key Takeaways
- Use recursion and backtracking to try all possible arrangements.
- Use a visited array to keep track of the numbers that have been used.
- Check the condition for each number before placing it in the arrangement.