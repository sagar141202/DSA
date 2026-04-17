# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "AGGTAB" and "GXTXAYB", the longest common subsequence is "GTAB". The sequences can contain any characters and have a maximum length of 1000.

## Approach
The Longest Common Subsequence problem can be solved using Dynamic Programming by creating a 2D table to store the lengths of common subsequences. The table is filled in a bottom-up manner, and the final result is stored in the last cell of the table. The algorithm has a time complexity of O(n*m), where n and m are the lengths of the two sequences.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string s1, string s2) {
    int n = s1.length();
    int m = s2.length();
    int dp[n + 1][m + 1];

    // Initialize the first row and column to 0
    for (int i = 0; i <= n; i++) {
        dp[i][0] = 0;
    }
    for (int j = 0; j <= m; j++) {
        dp[0][j] = 0;
    }

    // Fill the table in a bottom-up manner
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // The final result is stored in the last cell of the table
    return dp[n][m];
}

int main() {
    string s1 = "AGGTAB";
    string s2 = "GXTXAYB";
    cout << "Length of LCS: " << longestCommonSubsequence(s1, s2) << endl;
    return 0;
}
```

## Test Cases
```
Input: s1 = "AGGTAB", s2 = "GXTXAYB"
Output: 4
Input: s1 = "ABCBDAB", s2 = "BDCABA"
Output: 4
```

## Key Takeaways
- The Dynamic Programming approach is used to solve the Longest Common Subsequence problem efficiently.
- A 2D table is created to store the lengths of common subsequences, and the table is filled in a bottom-up manner.
- The final result is stored in the last cell of the table, which represents the length of the longest common subsequence.