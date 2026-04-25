# Longest Common Subsequence

## Problem Statement
The Longest Common Subsequence (LCS) problem is a classic problem in computer science and operations research that involves finding the longest sequence that appears in the same order in two or more sequences. Given two sequences X and Y, find the length of the longest common subsequence between X and Y. The sequences are composed of characters, and a subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements. For example, given X = "AGGTAB" and Y = "GXTXAYB", the longest common subsequence is "GTAB".

## Approach
The approach to solving this problem involves using dynamic programming to build a 2D table where each cell represents the length of the longest common subsequence up to that point in the sequences. The table is filled in row by row, with each cell depending on the values of the cells above and to the left. The final solution is stored in the bottom-right cell of the table.

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

    // Create a table to store lengths of longest common subsequences of substrings
    int dp[m + 1][n + 1];

    // Initialize the table
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            // If one of the strings is empty, the longest common subsequence is 0
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            }
            // If the current characters match, increase the length of the subsequence
            else if (X[i - 1] == Y[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            }
            // If the current characters do not match, consider the maximum length without the current character
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // The length of the longest common subsequence is stored in the bottom-right cell
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
- Dynamic programming is used to solve the LCS problem efficiently by avoiding redundant computations.
- The 2D table is used to store the lengths of the longest common subsequences of substrings, which helps in finding the final solution.
- The time complexity of the solution is O(m*n), where m and n are the lengths of the input sequences.