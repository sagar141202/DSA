# Longest Common Subsequence

## Problem Statement
The Longest Common Subsequence (LCS) problem is a classic problem in computer science and operations research that involves finding the longest sequence that appears in the same order in two or more sequences. Given two sequences X and Y, find the length of their LCS. The sequences are composed of characters, and the LCS should be a subsequence of both X and Y, not necessarily contiguous. For example, given X = "AGGTAB" and Y = "GXTXAYB", the LCS is "GTAB" with a length of 4.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell [i][j] represents the length of the LCS of the substrings X[0..i] and Y[0..j]. The LCS is constructed by comparing characters from X and Y and updating the table accordingly.

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
    int dp[m + 1][n + 1];

    // Initialize the first row and column to 0
    for (int i = 0; i <= m; i++) {
        dp[i][0] = 0;
    }
    for (int j = 0; j <= n; j++) {
        dp[0][j] = 0;
    }

    // Fill the dp table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // The length of the LCS is stored in the last cell of the dp table
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
- The dynamic programming approach is used to solve the LCS problem efficiently by avoiding redundant computations.
- The 2D dp table is used to store the lengths of LCS for subproblems, which helps in constructing the final LCS.
- The time complexity of the algorithm is O(m*n), where m and n are the lengths of the input sequences.