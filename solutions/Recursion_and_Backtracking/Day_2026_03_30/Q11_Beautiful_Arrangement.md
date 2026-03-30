# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, and you want to arrange them such that for every i (1 <= i <= N), the value at position i is either i times a factor of the value, or the value is a factor of i. Given an integer N, return the number of possible arrangements. For example, if N = 3, the possible arrangements are [1, 2, 3], [2, 1, 3], and [3, 2, 1], so the function should return 3.

## Approach
We will use backtracking to generate all possible arrangements and check if each arrangement satisfies the given condition. We will iterate over each position and try to place each number from 1 to N at that position, and then recursively try to fill the remaining positions.

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
        backtrack(1, N, count, visited);
        return count;
    }
    
    void backtrack(int pos, int N, int &count, vector<bool> &visited) {
        if (pos > N) {
            count++;
            return;
        }
        
        for (int i = 1; i <= N; i++) {
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
                visited[i] = true;
                backtrack(pos + 1, N, count, visited);
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
- Use backtracking to generate all possible arrangements of numbers from 1 to N.
- Check if each arrangement satisfies the given condition by verifying if the value at each position is either a factor of the position or the position is a factor of the value.
- Use a visited array to keep track of the numbers that have been used in the current arrangement.