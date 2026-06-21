# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "ABCBDAB" and "BDCABA", the longest common subsequence is "BCBA" with a length of 4. The sequences can contain any characters and the length of the sequences can be up to 1000 characters.

## Approach
The solution uses dynamic programming to build a 2D table where each cell [i][j] represents the length of the longest common subsequence of the first i characters of the first sequence and the first j characters of the second sequence. The algorithm fills the table in a bottom-up manner, comparing characters from both sequences and updating the table accordingly.

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
    // Create a 2D table to store lengths of longest common subsequences
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // If the current characters match, increase the length of the subsequence
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } 
            // If the characters do not match, consider the maximum length without the current character
            else {
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
    cout << "Length of the longest common subsequence: " << longestCommonSubsequence(s1, s2) << endl;
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
- The dynamic programming approach is suitable for solving problems with overlapping subproblems and optimal substructure.
- The 2D table helps to visualize and store the lengths of the longest common subsequences for subproblems.
- The time complexity is O(m*n) due to the nested loops used to fill the table, where m and n are the lengths of the input sequences.