# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA" with a length of 4. The sequences can contain any characters and have a maximum length of 1000.

## Approach
The Longest Common Subsequence (LCS) problem can be solved using Dynamic Programming, where we build a 2D table to store the lengths of common subsequences. We fill the table in a bottom-up manner by comparing characters from both sequences. If the characters match, we increment the length of the common subsequence.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string s1, string s2) {
    int m = s1.length();
    int n = s2.length();
    
    // Create a 2D table to store lengths of common subsequences
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // If characters match, increment the length of common subsequence
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } 
            // Otherwise, take the maximum length from the previous cells
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The length of the longest common subsequence is stored in the last cell
    return dp[m][n];
}

int main() {
    string s1 = "ABCBDAB";
    string s2 = "BDCABA";
    cout << "Length of LCS: " << longestCommonSubsequence(s1, s2);
    return 0;
}
```

## Test Cases
```
Input: s1 = "ABCBDAB", s2 = "BDCABA"
Output: 4
Input: s1 = "AGGTAB", s2 = "GXTXAYB"
Output: 4
```

## Key Takeaways
- The LCS problem can be solved using Dynamic Programming with a time complexity of O(m*n).
- The 2D table is used to store lengths of common subsequences, where each cell represents the length of the LCS up to that point.
- The final solution is stored in the last cell of the table.