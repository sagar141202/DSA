# Longest Common Subsequence

## Problem Statement
Given two sequences X and Y, find the length of the longest common subsequence (LCS) between them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, the LCS of "AGGTAB" and "GXTXAYB" is "GTAB". The sequences can contain any characters, and the length of the sequences is less than or equal to 1000. The goal is to find the length of the LCS and optionally reconstruct the LCS itself.

## Approach
The approach involves using dynamic programming to build a 2D table where each cell [i][j] represents the length of the LCS between the first i characters of X and the first j characters of Y. The algorithm iterates through the table, filling in the values based on whether the current characters in X and Y match or not.

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
    
    // Create a table to store lengths of longest common subsequences of substrings of X and Y
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
    
    // The length of the LCS is stored in the last cell of the table
    return dp[m][n];
}

// Function to print the LCS
void printLCS(string X, string Y) {
    int m = X.length();
    int n = Y.length();
    
    int dp[m + 1][n + 1];
    
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
    
    int i = m;
    int j = n;
    string lcs = "";
    
    while (i > 0 && j > 0) {
        if (X[i - 1] == Y[j - 1]) {
            lcs = X[i - 1] + lcs;
            i--;
            j--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }
    
    cout << "LCS: " << lcs << endl;
}

int main() {
    string X = "AGGTAB";
    string Y = "GXTXAYB";
    
    cout << "Length of LCS: " << longestCommonSubsequence(X, Y) << endl;
    printLCS(X, Y);
    
    return 0;
}
```

## Test Cases
```
Input: X = "AGGTAB", Y = "GXTXAYB"
Output: Length of LCS = 4, LCS = "GTAB"
```

## Key Takeaways
- The dynamic programming approach allows for an efficient solution with a time complexity of O(m*n), where m and n are the lengths of the input sequences.
- The space complexity is also O(m*n) due to the 2D table used to store the lengths of the LCS.
- The algorithm can be easily modified to print the LCS itself by backtracking through the table.