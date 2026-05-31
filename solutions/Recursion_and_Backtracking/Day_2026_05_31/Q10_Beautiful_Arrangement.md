# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n, and you want to arrange them in such a way that for every i (1 <= i <= n), the ith position is either divisible by i or i is divisible by the ith position. Find the total number of such arrangements. The input will be the number of integers n.

## Approach
The problem can be solved using backtracking, where we try to place each number from 1 to n in the current position if it satisfies the condition. We use a boolean array to keep track of the used numbers. The algorithm recursively tries all possible arrangements and counts the valid ones.

## Complexity
- Time: O(k), where k is the number of valid arrangements
- Space: O(n), for the recursion stack and the used array

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countArrangement(int n) {
        vector<bool> used(n + 1, false);
        int count = 0;
        backtrack(1, n, used, count);
        return count;
    }
    
    void backtrack(int index, int n, vector<bool>& used, int& count) {
        if (index > n) {
            count++;
            return;
        }
        
        for (int i = 1; i <= n; i++) {
            if (!used[i] && (index % i == 0 || i % index == 0)) {
                used[i] = true;
                backtrack(index + 1, n, used, count);
                used[i] = false;
            }
        }
    }
};
```

## Test Cases
```
Input: 2
Output: 2
```

## Key Takeaways
- Use backtracking to try all possible arrangements and count the valid ones.
- Use a boolean array to keep track of the used numbers to avoid duplicates.
- The time complexity is O(k), where k is the number of valid arrangements, because we only count the valid arrangements.