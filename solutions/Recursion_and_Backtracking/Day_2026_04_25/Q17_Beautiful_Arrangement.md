# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, we need to arrange them in such a way that for every i where 1 <= i <= N, the number at the i-th position is either i times a number or a number that i can divide. In other words, the number at position i should be a multiple of i or i should be a multiple of that number. We need to find the count of such arrangements. For example, for N = 3, the possible arrangements are [1, 2, 3], [2, 1, 3]. The constraints are 1 <= N <= 15.

## Approach
The problem can be solved using recursion and backtracking. We can try to place each number from 1 to N at each position and check if the number at the i-th position satisfies the given condition. If it does, we can move to the next position. If not, we can backtrack and try another number.

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
            if (!visited[i] && (pos % i == 0 || i % pos == 0)) {
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
Input: N = 2
Output: 2
Input: N = 3
Output: 3
```

## Key Takeaways
- Use recursion and backtracking to solve the problem.
- Use a visited array to keep track of the numbers that have been used.
- Check the condition for each number at each position before moving to the next position.