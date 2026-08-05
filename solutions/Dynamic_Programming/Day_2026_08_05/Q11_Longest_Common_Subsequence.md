# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA" with a length of 4. The sequences can contain any characters and have a maximum length of 1000.

## Approach
The Longest Common Subsequence problem can be solved using Dynamic Programming by creating a 2D table to store the lengths of common subsequences. The table is filled in a bottom-up manner, considering all possible substrings of the input sequences. The final solution is obtained by tracing back the table to construct the longest common subsequence.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestCommonSubsequence(string s1, string s2) {
    int m = s1.length();
    int n = s2.length();
    
    // Create a 2D table to store the lengths of common subsequences
    int dp[m + 1][n + 1];
    
    // Initialize the table with zeros
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            dp[i][j] = 0;
        }
    }
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The length of the longest common subsequence is stored in the last cell of the table
    return dp[m][n];
}

int main() {
    string s1 = "ABCBDAB";
    string s2 = "BDCABA";
    cout << "Length of longest common subsequence: " << longestCommonSubsequence(s1, s2);
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
- The Longest Common Subsequence problem has a wide range of applications in computer science, such as data compression, pattern recognition, and bioinformatics.
- Dynamic Programming is a suitable approach for solving this problem, as it allows for efficient computation of the lengths of common subsequences.
- The time complexity of the solution is O(m * n), where m and n are the lengths of the input sequences, making it efficient for large inputs.