# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases are generated so that the answer will be in the range of int.

## Approach
The problem can be solved by using dynamic programming to store the number of distinct subsequences. We create a 2D array where each cell [i][j] represents the number of distinct subsequences of the first i characters of S that are equal to the first j characters of T. We fill up this array by iterating over S and T.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.size(), n = t.size();
        vector<vector<long long>> dp(m + 1, vector<long long>(n + 1, 0));
        
        // initialize the base case
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[m][n];
    }
};
```

## Test Cases
```
Input: S = "rabbbit", T = "rabbit"
Output: 3
Input: S = "abc", T = "abc"
Output: 1
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems and optimal substructure.
- Initialize the base case correctly to avoid incorrect results.
- Fill up the dp array in a bottom-up manner to ensure that the previous results are available when needed.