# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, and you want to arrange them in a beautiful way, meaning that for every i, the adjacent element (i-1 or i+1) is either i-1 or i+1. Given an integer N, return the number of possible beautiful arrangements. Note that the arrangements are considered distinct if they are not identical, even if they are rotations or reflections of each other. For example, given N = 3, the possible beautiful arrangements are [1, 2, 3] and [1, 3, 2], so the function should return 3.

## Approach
The problem can be solved using recursion and backtracking, where we try to place each number from 1 to N in the arrangement and check if it leads to a valid beautiful arrangement. We use a visited array to keep track of the numbers that have been placed. The base case is when all numbers have been placed, in which case we increment the count of beautiful arrangements.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countArrangement(int N) {
        vector<bool> visited(N + 1, false);
        int count = 0;
        backtrack(1, N, visited, count);
        return count;
    }

    void backtrack(int pos, int N, vector<bool>& visited, int& count) {
        if (pos > N) {
            count++;
            return;
        }
        for (int i = 1; i <= N; i++) {
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
                visited[i] = true;
                backtrack(pos + 1, N, visited, count);
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
Output: 4
```

## Key Takeaways
- Use recursion and backtracking to explore all possible arrangements.
- Use a visited array to keep track of the numbers that have been placed.
- The base case is when all numbers have been placed, in which case we increment the count of beautiful arrangements.