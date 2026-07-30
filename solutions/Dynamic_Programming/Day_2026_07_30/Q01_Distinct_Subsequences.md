# Distinct Subsequences
## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The problem has the following constraints: 1 <= S.length, T.length <= 10^5, and S and T consist only of lowercase English letters. For example, if S = "rabbbit" and T = "rabbit", the output should be 3.

## Approach
The problem can be solved using dynamic programming, where we create a 2D table to store the number of distinct subsequences of S that are equal to T up to a certain position. We iterate over the strings S and T, and for each character, we check if it matches the current character in T. If it does, we update the table accordingly. The algorithm has a time complexity of O(m*n), where m and n are the lengths of S and T respectively.

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
        int m = s.length(), n = t.length();
        vector<vector<unsigned int>> dp(m + 1, vector<unsigned int>(n + 1, 0));
        
        // Initialize the base case
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If the current characters in S and T match, update the table
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    // If the characters do not match, the number of distinct subsequences remains the same
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
- The problem can be solved using dynamic programming with a time complexity of O(m*n), where m and n are the lengths of S and T respectively.
- The space complexity is also O(m*n) due to the 2D table used to store the number of distinct subsequences.
- The algorithm iterates over the strings S and T, and for each character, it checks if it matches the current character in T and updates the table accordingly.