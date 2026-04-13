# Beautiful Arrangement

## Problem Statement
Suppose you have n integers from 1 to n. We can arrange them into a sequence. When a number a is placed at position b, we say it is a beautiful arrangement if a can be divided by b or b can be divided by a. Given an integer n, return the number of possible beautiful arrangements that can be constructed. Constraints: 1 <= n <= 15.

## Approach
We will use recursion and backtracking to try all possible arrangements and count the beautiful ones. The key idea is to place each number from 1 to n at each position and check if it's a beautiful arrangement. We will use a helper function to perform the recursion and backtracking.

## Complexity
- Time: O(k), where k is the number of possible arrangements (upper bound is n!)
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
            if (!used[i] && (i % index == 0 || index % i == 0)) {
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
Input: n = 3
Output: 3
Explanation: 
There are 3 possible beautiful arrangements: 
[1, 2, 3], 
[2, 1, 3], 
[3, 1, 2]
```

## Key Takeaways
- Recursion and backtracking can be used to try all possible arrangements.
- The key idea is to use a helper function to perform the recursion and backtracking.
- We need to use a used array to keep track of the numbers that have been used.