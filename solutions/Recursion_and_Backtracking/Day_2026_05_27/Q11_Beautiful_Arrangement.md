# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n. We can arrange them into a circle in n! ways. We want to find the number of arrangements where for every i (1 <= i <= n), the ith number is either a multiple of i or i is a multiple of the ith number. For example, if n = 3, we have 3 possible arrangements: [1, 2, 3], [1, 3, 2], and [2, 1, 3]. If n = 4, we have 2 possible arrangements: [1, 2, 4, 3] and [1, 3, 4, 2]. Given an integer n, find the number of beautiful arrangements.

## Approach
To solve this problem, we will use backtracking to generate all possible arrangements and then check each one to see if it satisfies the condition. We will start by placing the first number in the first position, and then recursively try to place the remaining numbers in the remaining positions.

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
- The problem requires backtracking to generate all possible arrangements.
- The time complexity is O(n!) due to the recursive nature of the solution.
- The space complexity is O(n) for storing the visited array.