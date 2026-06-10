# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them such that for every i (1 <= i <= n), the number at position i is a multiple of i or i is a multiple of the number at position i. Given an integer n, return the number of possible arrangements. For example, if n = 3, the possible arrangements are [1, 2, 3], [2, 1, 3], and [3, 2, 1]. If n = 4, there are no possible arrangements.

## Approach
The problem can be solved using backtracking, where we try to place each number from 1 to n at each position and check if the arrangement is valid. We use a visited array to keep track of the numbers that have been used. The algorithm recursively tries all possible arrangements and counts the valid ones.

## Complexity
- Time: O(k), where k is the number of possible arrangements
- Space: O(n), where n is the input integer

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
Input: n = 4
Output: 0
```

## Key Takeaways
- Use backtracking to try all possible arrangements of numbers.
- Use a visited array to keep track of the numbers that have been used.
- Check if the current arrangement is valid by verifying the condition for each position.