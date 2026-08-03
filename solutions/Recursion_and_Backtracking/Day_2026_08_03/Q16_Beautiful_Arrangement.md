# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in such a way that for every i, the ith integer is either divisible by i or i is divisible by the ith integer. Given an integer n, count the number of beautiful arrangements that can be made. The input will be an integer n, where 1 <= n <= 15. For example, if n = 3, the beautiful arrangements are [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].

## Approach
We can use recursion and backtracking to solve this problem. The idea is to try each number from 1 to n at each position and check if the current arrangement is valid. If it is, we continue to the next position; otherwise, we backtrack and try the next number.

## Complexity
- Time: O(k), where k is the number of valid arrangements
- Space: O(n), for the recursion stack

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
        if (index == n + 1) {
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
Input: n = 4
Output: 4
```

## Key Takeaways
- Use recursion and backtracking to explore all possible arrangements
- Use a visited array to keep track of the numbers that have been used
- Use a condition to check if the current arrangement is valid before continuing to the next position