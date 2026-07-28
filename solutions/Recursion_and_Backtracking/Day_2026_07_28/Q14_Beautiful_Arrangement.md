# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in a way that for every i, either the number at position i is i, or the number at position i is a multiple of i. Given an integer n, return the number of beautiful arrangements that can be made. For example, if n = 3, there are 3 beautiful arrangements: [1, 2, 3], [1, 3, 2], and [2, 1, 3] are not valid, but [1, 3, 2] and [3, 1, 2] are not valid, only [1, 2, 3] is valid, and there are two other valid arrangements: [2, 3, 1] is not valid, only [3, 1, 2] is not valid, only [1, 3, 2] is not valid. The valid ones are [1, 2, 3] and [1, 3, 2]. So the answer for n = 3 is 3.

## Approach
We will solve this problem using recursion and backtracking, checking all possible permutations of the numbers from 1 to n and counting the ones that satisfy the condition. We will use a visited array to keep track of the numbers that have been used.

## Complexity
- Time: O(n!)
- Space: O(n)

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
Input: n = 3
Output: 3
```

## Key Takeaways
- Recursion and backtracking can be used to solve problems that involve counting the number of ways to arrange objects under certain constraints.
- Using a visited array can help keep track of the objects that have been used.
- The time complexity of this solution is O(n!) because we are generating all permutations of the numbers from 1 to n.