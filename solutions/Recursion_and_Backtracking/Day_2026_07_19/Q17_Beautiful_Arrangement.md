# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a beautiful way such that for every i, the adjacent element (i-1 or i+1) is either i-1 or i+1 mod n. Given an integer n, return the number of possible arrangements. Note that the arrangements are considered distinct if they are not identical when rotated or reflected.

## Approach
The problem can be solved using recursion and backtracking by trying all possible arrangements of numbers. We start by placing the first number and then recursively try to place the remaining numbers in a valid arrangement. If a valid arrangement is found, we increment the count of arrangements.

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
Input: n = 2
Output: 2
Input: n = 3
Output: 3
```

## Key Takeaways
- Recursion and backtracking are useful for solving problems that involve trying all possible arrangements or combinations.
- The time complexity of recursive solutions can be high due to the repeated computation of subproblems.
- Using a visited array to keep track of used elements can help avoid duplicate arrangements.