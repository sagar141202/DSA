# Longest Common Subsequence

## Problem Statement
The Longest Common Subsequence (LCS) problem is a classic problem in computer science and operations research that involves finding the longest sequence common to two or more sequences. Given two sequences X and Y, find the length of their LCS. The LCS problem has numerous applications in data comparison, bioinformatics, and text processing. For example, given two sequences "AGGTAB" and "GXTXAYB", the LCS is "GTAB" with a length of 4.

## Approach
The LCS problem can be solved using dynamic programming, where we build a 2D table to store the lengths of common subsequences. We fill the table in a bottom-up manner, considering all possible subsequences of the input sequences. The final solution is obtained by tracing back the table from the bottom-right corner to the top-left corner.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lcs(string X, string Y, int m, int n) {
    // Create a table to store lengths of longest common subsequences of substrings
    int dp[m + 1][n + 1];

    // Initialize the table with zeros
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            }
        }
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

    // The length of the LCS is stored in the bottom-right corner of the table
    return dp[m][n];
}

int main() {
    string X = "AGGTAB";
    string Y = "GXTXAYB";
    int m = X.length();
    int n = Y.length();

    cout << "Length of LCS: " << lcs(X, Y, m, n) << endl;

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
- The LCS problem can be solved using dynamic programming with a time complexity of O(m*n).
- The space complexity of the solution is O(m*n) due to the 2D table used to store the lengths of common subsequences.
- The solution involves filling the table in a bottom-up manner and tracing back the table to obtain the final solution.