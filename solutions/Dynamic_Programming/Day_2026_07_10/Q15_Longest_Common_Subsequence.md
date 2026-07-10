# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA" with a length of 4. The sequences can be strings or arrays of integers.

## Approach
The Longest Common Subsequence (LCS) problem can be solved using dynamic programming, where we build a 2D table to store the lengths of common subsequences. We iterate through both sequences, comparing characters and updating the table accordingly. The final solution is the value in the bottom-right corner of the table.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string s1, string s2) {
    int m = s1.size();
    int n = s2.size();
    // Create a 2D table to store lengths of common subsequences
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    // Iterate through both sequences
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // If characters match, update the length of the common subsequence
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } 
            // If characters do not match, take the maximum length from the previous cells
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    // The final solution is the value in the bottom-right corner of the table
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
- The dynamic programming approach is suitable for solving the LCS problem, as it avoids redundant computations and has a time complexity of O(m*n).
- The 2D table `dp` is used to store the lengths of common subsequences, where `dp[i][j]` represents the length of the LCS of the first `i` characters of `s1` and the first `j` characters of `s2`.
- The final solution is the value in the bottom-right corner of the table, which represents the length of the LCS of the entire input sequences.