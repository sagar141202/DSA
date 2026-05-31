# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`. A palindromic subsequence is a subsequence that reads the same backwards as forwards. For example, "aba" is a palindromic subsequence, but "abc" is not. The input string `s` will have a length between 1 and 1000 characters, and it will only contain lowercase English letters.

## Approach
We will use dynamic programming to solve this problem by building a 2D table where each cell `[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`. We will fill this table in a bottom-up manner, starting from the substrings of length 1 and 2.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestPalindromicSubseq(string s) {
        int n = s.size();
        // Create a 2D table to store the lengths of palindromic subsequences
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // Initialize the diagonal of the table with 1s
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill the table in a bottom-up manner
        for (int length = 2; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                if (s[i] == s[j]) {
                    // If the characters at the ends are the same, add 2 to the length of the subsequence
                    dp[i][j] = dp[i + 1][j - 1] + 2;
                } else {
                    // If the characters at the ends are different, take the maximum length of the subsequences without the ends
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
                }
            }
        }
        
        // The length of the longest palindromic subsequence is stored in the top-right corner of the table
        return dp[0][n - 1];
    }
};
```

## Test Cases
```
Input: "bbbab"
Output: 4
Input: "cbbd"
Output: 2
```

## Key Takeaways
- The dynamic programming approach is suitable for problems that have overlapping subproblems and optimal substructure.
- The 2D table `dp` is used to store the lengths of palindromic subsequences, where `dp[i][j]` represents the length of the longest palindromic subsequence in the substring `s[i...j]`.
- The time complexity of the solution is O(n^2), where n is the length of the input string `s`.