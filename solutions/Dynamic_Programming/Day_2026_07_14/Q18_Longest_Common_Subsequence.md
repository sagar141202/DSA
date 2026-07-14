# Longest Common Subsequence

## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "AGGTAB" and "GXTXAYB", the longest common subsequence is "GTAB". The problem has constraints such as 1 <= length of sequence 1, sequence 2 <= 1000, and the sequences only contain uppercase English letters.

## Approach
The algorithm uses Dynamic Programming to build a 2D table where each cell represents the length of the longest common subsequence up to that point. It iterates through both sequences, comparing characters and updating the table accordingly. The final result is stored in the bottom-right cell of the table.

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
            // If current characters match, increase length of subsequence
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } 
            // Otherwise, take the maximum length from the previous cells
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The length of the longest common subsequence is stored in the bottom-right cell
    return dp[m][n];
}

int main() {
    string s1 = "AGGTAB";
    string s2 = "GXTXAYB";
    cout << "Length of longest common subsequence: " << longestCommonSubsequence(s1, s2);
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
- The Dynamic Programming approach is particularly effective for problems with overlapping subproblems, like the Longest Common Subsequence.
- The 2D table helps to visualize and store the lengths of common subsequences, making it easier to derive the final result.
- The time and space complexities are both O(m*n), where m and n are the lengths of the input sequences.