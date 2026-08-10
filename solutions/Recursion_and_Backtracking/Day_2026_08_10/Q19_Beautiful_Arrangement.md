# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a way that for every i, either the number at position i is i, or the number at position i is a factor of i. Given an integer n, return the number of beautiful arrangements that can be made. For example, given n = 3, the beautiful arrangements are [1, 2, 3] and [1, 3, 2], so the function should return 3.

## Approach
The problem can be solved using recursion and backtracking. We will try to place each number from 1 to n at each position and check if it is a beautiful arrangement. If it is, we will recursively try to fill the rest of the positions. The base case is when all positions are filled.

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
        if (index > n) {
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
Input: n = 4
Output: 4
```

## Key Takeaways
- Use recursion and backtracking to try all possible arrangements.
- Use a visited array to keep track of the numbers that have been used.
- The base case is when all positions are filled, in which case we increment the count of beautiful arrangements.