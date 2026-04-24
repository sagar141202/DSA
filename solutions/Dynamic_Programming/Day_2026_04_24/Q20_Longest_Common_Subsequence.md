# Longest Common Subsequence

## Problem Statement
The Longest Common Subsequence (LCS) problem is a classic problem in computer science and operations research that involves finding the longest sequence that appears in the same order in two or more sequences. Given two sequences X and Y, find the length of their LCS. The sequences are composed of characters, and the LCS should be a subsequence of both X and Y, not necessarily a substring. For example, if X = "AGGTAB" and Y = "GXTXAYB", the LCS is "GTAB" with a length of 4.

## Approach
The LCS problem can be solved using dynamic programming, where we build a 2D table to store the lengths of LCS for subproblems. We fill the table in a bottom-up manner, considering whether the current characters in the sequences match or not.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lcs(string X, string Y, int m, int n) {
    // Create a table to store lengths of LCS
    int dp[m + 1][n + 1];

    // Fill the table in a bottom-up manner
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            // If either sequence is empty, LCS length is 0
            if (i == 0 || j == 0)
                dp[i][j] = 0;
            // If current characters match, consider it in LCS
            else if (X[i - 1] == Y[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            // If current characters do not match, consider the max of two cases
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    // The length of LCS is stored in the last cell of the table
    return dp[m][n];
}

int main() {
    string X = "AGGTAB";
    string Y = "GXTXAYB";
    int m = X.size();
    int n = Y.size();
    cout << "Length of LCS is " << lcs(X, Y, m, n);
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
- The LCS problem can be solved using dynamic programming with a time complexity of O(m*n), where m and n are the lengths of the input sequences.
- The space complexity is also O(m*n) due to the 2D table used to store the lengths of LCS for subproblems.
- The LCS problem has various applications in data comparison, bioinformatics, and text processing.