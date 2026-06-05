# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases will be such that the answer will always be less than or equal to 2^31 - 1. For example, if S = "rabbbit" and T = "rabbit", then there are 3 distinct subsequences: "rabbbit" -> "rabbit" (by removing the second 'b' and the second 'b'), "rabbbit" -> "rabbit" (by removing the first 'b' and the second 'b'), and "rabbbit" -> "rabbit" (by removing the first 'b' and the first 'b'). 

## Approach
We will use dynamic programming to solve this problem, where dp[i][j] represents the number of distinct subsequences of the first i characters of S that are equal to the first j characters of T. We will iterate over the characters of S and T, and for each character, we will check if it matches the current character in T. If it does, we will update dp[i][j] accordingly.

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
        
        // Initialize the base case
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
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The time complexity of the solution is O(m*n), where m and n are the lengths of the strings S and T, respectively.
- The space complexity of the solution is O(m*n), which is the size of the dp table.