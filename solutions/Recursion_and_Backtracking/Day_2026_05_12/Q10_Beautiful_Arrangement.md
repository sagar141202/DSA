# Beautiful Arrangement

## Problem Statement
Suppose you have n integers labeled from 1 to n. A beautiful arrangement is when the numbers are arranged such that for every i, either i is a multiple of the number at position i, or the number at position i is a multiple of i. Given an integer n, return the number of beautiful arrangements that can be made. For example, if n = 3, the beautiful arrangements are [1, 2, 3], [1, 3, 2]. The constraint is 1 <= n <= 15.

## Approach
The problem can be solved using recursion and backtracking. We will try to place each number from 1 to n at each position and check if the current arrangement is beautiful. If it is, we will continue to the next position. If not, we will backtrack and try a different number.

## Complexity
- Time: O(k) where k is the number of beautiful arrangements, which can be up to n! in the worst case
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
Input: n = 3
Output: 3
Input: n = 4
Output: 4
```

## Key Takeaways
- Use recursion and backtracking to try all possible arrangements of numbers
- Use a visited array to keep track of numbers that have been used
- Check if the current arrangement is beautiful by verifying the multiple condition for each position