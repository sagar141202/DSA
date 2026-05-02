# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, we need to find the number of possible arrangements of these integers such that for every i, the ith integer is either divisible by i or i is divisible by the ith integer. For example, if n = 3, then the possible arrangements are [1, 2, 3] and [2, 1, 3] and [3, 1, 2] and so on. 1 <= n <= 15.

## Approach
The problem can be solved using recursion and backtracking. We can try to place each number from 1 to n at each position and check if the current arrangement is valid. If it is valid, we continue to the next position; otherwise, we backtrack and try the next number.

## Complexity
- Time: O(k) where k is the number of valid arrangements
- Space: O(n) for the recursion stack

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
```

## Key Takeaways
- Use recursion and backtracking to generate all possible arrangements.
- Use a visited array to keep track of the numbers that have been used in the current arrangement.
- Check if the current arrangement is valid by verifying if the ith integer is either divisible by i or i is divisible by the ith integer.