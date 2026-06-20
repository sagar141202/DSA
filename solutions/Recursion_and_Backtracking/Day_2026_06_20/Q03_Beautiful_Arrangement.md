# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, we need to find the number of possible arrangements of these integers such that for every i, the integer at position i is a multiple of i or i is a multiple of the integer at position i. For example, if N = 3, then the possible arrangements are [1,2,3], [2,1,3], [3,1,2]. We need to find the total number of such arrangements for a given N.

## Approach
We will use backtracking to solve this problem, trying all possible numbers at each position and checking if the current number satisfies the condition. If it does, we move to the next position; otherwise, we backtrack and try the next number.

## Complexity
- Time: O(k), where k is the number of possible arrangements, which in the worst case is O(N!)
- Space: O(N), for the recursion stack

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
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
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
Input: N = 3
Output: 3
Input: N = 4
Output: 4
```

## Key Takeaways
- Use backtracking to try all possible arrangements and check the condition for each position.
- Use a visited array to keep track of the numbers that have been used.
- The time complexity is O(k), where k is the number of possible arrangements, which can be very large for large inputs.