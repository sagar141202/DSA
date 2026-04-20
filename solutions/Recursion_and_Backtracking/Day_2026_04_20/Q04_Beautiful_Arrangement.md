# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, we need to find the number of possible arrangements of these integers such that for every i, the ith integer is either divisible by i or i is divisible by the ith integer. For example, if n = 3, then the possible arrangements are [1,2,3], [2,1,3], and [3,1,2]. The input will be an integer n and the output should be the total number of possible arrangements.

## Approach
The problem can be solved using recursion and backtracking, where we try to place each number from 1 to n at each position and check if the current arrangement is valid. We use a boolean array to keep track of the numbers that have been used.

## Complexity
- Time: O(k), where k is the number of possible arrangements
- Space: O(n), for the recursion stack and the boolean array

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
Input: 3
Output: 3
Input: 4
Output: 4
```

## Key Takeaways
- Use recursion and backtracking to solve the problem
- Keep track of the used numbers to avoid duplicates
- Check the divisibility condition for each number at each position