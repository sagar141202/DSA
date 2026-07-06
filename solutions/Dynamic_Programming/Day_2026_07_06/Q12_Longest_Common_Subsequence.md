# Longest Common Subsequence

## Problem Statement
The Longest Common Subsequence (LCS) problem is a classic problem in computer science and operations research that involves finding the longest sequence that appears in the same order in two or more sequences. Given two sequences X and Y, find the length of their LCS. The sequences are composed of characters, and the LCS should be a contiguous subsequence of both sequences. For example, given X = "AGGTAB" and Y = "GXTXAYB", the LCS is "GTAB" with a length of 4.

## Approach
The approach to solve this problem is to use Dynamic Programming (DP) to build a 2D table where each cell [i][j] represents the length of the LCS of the substrings X[0..i] and Y[0..j]. The algorithm fills the table in a bottom-up manner, comparing characters from both sequences and updating the table accordingly.

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
    
    // Create a 2D table to store lengths of LCS
    int dp[m + 1][n + 1];
    
    // Initialize the first row and column to 0
    for (int i = 0; i <= m; i++) {
        dp[i][0] = 0;
    }
    for (int j = 0; j <= n; j++) {
        dp[0][j] = 0;
    }
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The length of LCS is stored in the last cell
    return dp[m][n];
}

int main() {
    string X = "AGGTAB";
    string Y = "GXTXAYB";
    cout << "Length of LCS: " << longestCommonSubsequence(X, Y);
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
- The Dynamic Programming approach is efficient for solving the LCS problem with a time complexity of O(m*n), where m and n are the lengths of the input sequences.
- The 2D table helps to avoid redundant computations by storing the lengths of LCS for subproblems.
- The algorithm can be easily modified to reconstruct the actual LCS by tracing back the table from the last cell to the first cell.