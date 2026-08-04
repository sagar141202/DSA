# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a way that for every i, the ith number is either divisible by i or i is divisible by the ith number. Find the number of beautiful arrangements that can be formed. The input is an integer n, and the output is the number of beautiful arrangements.

## Approach
The problem can be solved using backtracking, where we try each number from 1 to n at each position and check if the current arrangement is valid. We use a visited array to keep track of the numbers that have been used. The base case is when all numbers have been used, in which case we increment the count of beautiful arrangements.

## Complexity
- Time: O(k), where k is the number of possible arrangements
- Space: O(n), where n is the input number

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
Input: 2
Output: 2
Input: 3
Output: 3
```

## Key Takeaways
- Use backtracking to try all possible arrangements of numbers.
- Use a visited array to keep track of the numbers that have been used.
- The base case is when all numbers have been used, in which case we increment the count of beautiful arrangements.