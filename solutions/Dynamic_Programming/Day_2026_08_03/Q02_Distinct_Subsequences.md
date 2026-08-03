# Distinct Subsequences

## Problem Statement
Given a string S and a string T, count the number of distinct subsequences of S that are equal to T. A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. The test cases are generated so that the answer will fit in a 32-bit integer.

## Approach
We will use dynamic programming to solve this problem by maintaining a 2D array where each cell represents the number of distinct subsequences of the substring S[0..i] that are equal to the substring T[0..j]. We will fill up this array in a bottom-up manner.

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
        int n = s.size();
        int m = t.size();
        
        // Create a 2D array to store the number of distinct subsequences
        vector<vector<unsigned int>> dp(n + 1, vector<unsigned int>(m + 1, 0));
        
        // Initialize the base case where T is an empty string
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }
        
        // Fill up the dp array in a bottom-up manner
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // If the current characters in S and T are the same, 
                // we have two options: include the current character in S or not
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } 
                // If the current characters in S and T are different, 
                // we cannot include the current character in S
                else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        
        // The answer is stored in the last cell of the dp array
        return dp[n][m];
    }
};
```

## Test Cases
```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Input: s = "abcd", t = "abcd"
Output: 1
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The time complexity of this solution is O(n*m) where n and m are the lengths of the strings S and T respectively.
- The space complexity of this solution is O(n*m) which is used to store the dp array.