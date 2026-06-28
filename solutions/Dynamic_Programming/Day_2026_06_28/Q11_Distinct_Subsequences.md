# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that equals T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases are generated so that the answer is guaranteed to fit in a 32-bit integer.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array where each cell [i][j] represents the number of distinct subsequences of the first i characters in S that equals the first j characters in T. We iterate over the strings and update the array based on whether the current characters match or not.

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
        vector<vector<unsigned int>> dp(n + 1, vector<unsigned int>(m + 1, 0));
        
        // Initialize the base case where T is an empty string
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If the current characters match, consider two cases: 
                // include the current character in the subsequence or not
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } 
                // If the current characters do not match, do not include the current character in the subsequence
                else {
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
Input: S = "subscription", T = "subscription"
Output: 1
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems and optimal substructure.
- The time complexity of dynamic programming solutions is often O(n*m) where n and m are the sizes of the input strings.
- The space complexity of dynamic programming solutions is often O(n*m) as well, where n and m are the sizes of the input strings.