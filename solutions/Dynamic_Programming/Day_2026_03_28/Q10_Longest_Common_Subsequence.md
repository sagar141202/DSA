# Longest Common Subsequence
## Problem Statement
Given two sequences, find the length of the longest subsequence common to both of them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example, given two sequences "AGGTAB" and "GXTXAYB", the longest common subsequence is "GTAB". The sequences can contain any characters and can be of any length up to 1000.

## Approach
The approach to solve this problem is to use dynamic programming, where we build a 2D table to store the lengths of the longest common subsequences of subproblems. We fill the table in a bottom-up manner, considering all possible cases of character matches and mismatches.

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
    // Create a 2D table to store the lengths of the longest common subsequences
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // If the current characters match, consider it as part of the subsequence
            if (s1[i - 1] == s2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } 
            // If the current characters do not match, consider the maximum length without it
            else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The length of the longest common subsequence is stored in the bottom-right corner of the table
    return dp[m][n];
}

int main() {
    string s1 = "AGGTAB";
    string s2 = "GXTXAYB";
    cout << "Length of the longest common subsequence: " << longestCommonSubsequence(s1, s2);
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
- The longest common subsequence problem can be solved using dynamic programming with a time complexity of O(m*n), where m and n are the lengths of the input sequences.
- The space complexity is also O(m*n) due to the 2D table used to store the lengths of the longest common subsequences of subproblems.
- The solution involves filling the table in a bottom-up manner, considering all possible cases of character matches and mismatches.