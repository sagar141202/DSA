# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The length of S is less than or equal to 100, and the length of T is less than or equal to 100. For example, if S = "rabbbit" and T = "rabbit", the output should be 3.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of distinct subsequences. We iterate over the strings S and T, and for each character, we check if it matches or not. If it matches, we add the number of distinct subsequences without the current character to the current cell. If it does not match, we simply copy the value from the previous cell.

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
        vector<vector<unsigned int>> dp(m + 1, vector<unsigned int>(n + 1, 0));
        
        // Initialize the base case
        for (int j = 0; j <= n; j++) {
            dp[0][j] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If the current characters match, add the number of distinct subsequences without the current character
                if (t[i - 1] == s[j - 1]) {
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1];
                } 
                // If the current characters do not match, copy the value from the previous cell
                else {
                    dp[i][j] = dp[i][j - 1];
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
Input: S = "abc", T = "def"
Output: 0
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The time complexity of the solution is O(n*m), where n and m are the lengths of the strings S and T respectively.
- The space complexity of the solution is O(n*m), which is used to store the 2D table.