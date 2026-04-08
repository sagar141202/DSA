# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, and you want to arrange them in a beautiful way. A beautiful arrangement is one where for every i, the number at position i is either a multiple of i or i is a multiple of the number at position i. Given an integer N, return the number of beautiful arrangements that can be constructed. For example, if N = 3, the beautiful arrangements are [1, 2, 3], [1, 3, 2]. If N = 4, the beautiful arrangements are [1, 2, 3, 4], [1, 3, 2, 4], [1, 2, 4, 3], [1, 4, 2, 3], [1, 4, 3, 2], [1, 3, 4, 2].

## Approach
We can solve this problem using backtracking. The idea is to try each number from 1 to N at each position and check if the current arrangement is beautiful. If it is, we move on to the next position; otherwise, we backtrack and try the next number.

## Complexity
- Time: O(k) where k is the number of beautiful arrangements, because in the worst case, we have to generate all possible arrangements.
- Space: O(N) for the recursion stack.

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
- Use backtracking to generate all possible arrangements and check if each arrangement is beautiful.
- Use a visited array to keep track of the numbers that have been used in the current arrangement.
- The base case for the backtracking is when the position is greater than N, in which case we increment the count of beautiful arrangements.