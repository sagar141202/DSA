# Longest Common Subsequence

## Problem Statement
The Longest Common Subsequence (LCS) problem is a classic problem in computer science and operations research that involves finding the longest sequence that appears in the same order in two or more sequences. Given two sequences X and Y, find the length of their LCS. The sequences are composed of characters, and the LCS should be a contiguous subsequence of both sequences. For example, given X = "AGGTAB" and Y = "GXTXAYB", the LCS is "GTAB" with a length of 4.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents the length of the LCS of the substrings X[0..i] and Y[0..j]. The final result is stored in the bottom-right cell of the table. The intuition behind this approach is to break down the problem into smaller subproblems and store their solutions to avoid redundant computation.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string X, string Y) {
    int m = X.size();
    int n = Y.size();
    
    // Create a table to store lengths of LCS of substrings of X and Y
    int dp[m + 1][n + 1];
    
    // Initialize the table
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            } else if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The length of LCS is stored in the bottom-right cell of the table
    return dp[m][n];
}

int main() {
    string X = "AGGTAB";
    string Y = "GXTXAYB";
    cout << "Length of LCS: " << longestCommonSubsequence(X, Y) << endl;
    return 0;
}
```

## Test Cases
```
Input: X = "AGGTAB", Y = "GXTXAYB"
Output: 4
Input: X = "ABCBDAB", Y = "BDCABA"
Output: 4
```

## Key Takeaways
- The dynamic programming approach is used to solve the LCS problem efficiently by avoiding redundant computation.
- The 2D table is used to store the lengths of LCS of substrings of the input sequences.
- The final result is stored in the bottom-right cell of the table, which represents the length of the LCS of the entire input sequences.