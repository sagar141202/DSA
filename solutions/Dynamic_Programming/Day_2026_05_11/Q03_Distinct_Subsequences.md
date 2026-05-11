# Distinct Subsequences
## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The problem has the following constraints: 1 <= S.length, T.length <= 10^5, and the strings only contain lowercase English letters.

## Approach
The problem can be solved using dynamic programming, where we build a 2D array dp of size (S.length + 1) x (T.length + 1), and dp[i][j] represents the number of distinct subsequences of S.substring(0, i) that equals T.substring(0, j). We fill up the dp array by considering two cases: whether the current character in S matches the current character in T or not.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.length(), n = t.length();
        vector<vector<unsigned long long>> dp(m + 1, vector<unsigned long long>(n + 1, 0));
        
        // Initialize base case
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If the current character in S matches the current character in T
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
Input: S = "abcd", T = "abcd"
Output: 1
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize the base case carefully to avoid incorrect results.
- Consider all possible cases when filling up the dp array to ensure correctness.