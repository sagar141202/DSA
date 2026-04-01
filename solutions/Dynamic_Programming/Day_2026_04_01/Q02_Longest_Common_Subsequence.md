# Longest Common Subsequence

## Problem Statement
The Longest Common Subsequence (LCS) problem is a classic problem in computer science and operations research that involves finding the longest sequence that appears in the same order in two or more sequences. Given two sequences X and Y, find the length of the longest subsequence common to both of them. For example, if X = "AGGTAB" and Y = "GXTXAYB", the LCS is "GTAB" with a length of 4. The problem has a wide range of applications, including data compression, bioinformatics, and text processing. The goal is to develop an efficient algorithm to solve the LCS problem for two sequences of lengths m and n.

## Approach
The approach to solve the LCS problem is to use dynamic programming, which involves breaking down the problem into smaller sub-problems and storing the solutions to these sub-problems to avoid redundant computation. The algorithm constructs a 2D table where each cell [i][j] represents the length of the LCS of the first i characters in sequence X and the first j characters in sequence Y.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string X, string Y) {
    int m = X.length();
    int n = Y.length();
    
    // Create a 2D table to store lengths of LCS
    int dp[m + 1][n + 1];
    
    // Initialize the first row and column to 0
    for (int i = 0; i <= m; i++)
        dp[i][0] = 0;
    for (int j = 0; j <= n; j++)
        dp[0][j] = 0;
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (X[i - 1] == Y[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    
    // The length of LCS is stored in the last cell
    return dp[m][n];
}

int main() {
    string X = "AGGTAB";
    string Y = "GXTXAYB";
    cout << "Length of LCS is " << longestCommonSubsequence(X, Y);
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
- Dynamic programming is an efficient approach to solve the LCS problem by breaking it down into smaller sub-problems and storing their solutions.
- The time complexity of the LCS algorithm using dynamic programming is O(m*n), where m and n are the lengths of the input sequences.
- The space complexity is also O(m*n) due to the 2D table used to store the lengths of LCS.