# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a way that for every i (1 <= i <= n), the number at position i is either a multiple of i or i is a multiple of the number at position i. Given an integer n, return the number of beautiful arrangements that can be made. For example, if n = 3, the beautiful arrangements are [1, 2, 3], [1, 3, 2]. If n = 4, the beautiful arrangements are [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 4, 3], [2, 1, 3, 4], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1].

## Approach
We can use backtracking to solve this problem, where we try to place each number from 1 to n in each position. If the current number can be placed at the current position (i.e., it is a multiple of the position or the position is a multiple of the number), we make a recursive call to fill the rest of the positions.

## Complexity
- Time: O(k), where k is the number of beautiful arrangements
- Space: O(n), for the recursion stack and the current arrangement

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
Output: 24
```

## Key Takeaways
- Use backtracking to try all possible arrangements of numbers from 1 to n.
- Check if the current number can be placed at the current position before making a recursive call.
- Use a visited array to keep track of the numbers that have been used in the current arrangement.