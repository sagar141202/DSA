# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a beautiful way. A beautiful arrangement is one where for every i (1 <= i <= n), the number at position i is either a multiple of i or i is a multiple of the number at position i. Given an integer n, return the number of beautiful arrangements that can be constructed. Note that the integers from 1 to n should be used exactly once in each arrangement.

## Approach
The problem can be solved using recursion and backtracking. We start with an empty arrangement and try to place each number from 1 to n at the current position. If the current number satisfies the condition for a beautiful arrangement, we recursively try to fill the rest of the positions. If not, we backtrack and try the next number.

## Complexity
- Time: O(k) where k is the number of valid permutations
- Space: O(n) for the recursion stack and the arrangement

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
Input: n = 2
Output: 2
Explanation: The two beautiful arrangements are [1,2] and [2,1].
Input: n = 3
Output: 3
Explanation: The three beautiful arrangements are [1,2,3], [2,1,3], and [3,1,2].
```

## Key Takeaways
- The recursion and backtracking approach can be used to solve problems that involve finding all possible permutations or combinations that satisfy certain conditions.
- The use of a visited array or vector can help avoid duplicate calculations and improve the efficiency of the solution.
- The base case for the recursion should be carefully defined to ensure that the function terminates correctly.