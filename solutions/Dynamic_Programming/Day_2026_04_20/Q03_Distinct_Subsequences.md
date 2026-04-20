# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not. The length of S is less than or equal to 100, and the length of T is less than or equal to 100.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell [i][j] represents the number of distinct subsequences of the first i characters of S that equals the first j characters of T. We fill up this array in a bottom-up manner. If the current character in S matches the current character in T, we have two options: either include the current character in the subsequence or not.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numDistinct(string s, string t) {
        int n = s.size(), m = t.size();
        vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, 0));
        
        // Initialize the base case
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        return dp[n][m];
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The problem can be broken down into smaller subproblems and the solutions to these subproblems can be stored in a table for future reference.
- The time complexity of the solution is O(n*m), where n and m are the lengths of the strings S and T respectively.