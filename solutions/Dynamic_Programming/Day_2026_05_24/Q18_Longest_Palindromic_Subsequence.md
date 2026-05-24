# Longest Palindromic Subsequence

## Problem Statement
Given a string, find the length of the longest palindromic subsequence. A palindromic subsequence is a sequence that reads the same backward as forward. The input string can contain lowercase English letters. The length of the input string is between 1 and 1000 characters. For example, given the string "banana", the longest palindromic subsequence is "anana" with a length of 5.

## Approach
The solution uses dynamic programming to build a 2D table where each cell [i][j] represents the length of the longest palindromic subsequence in the substring from index i to j. The algorithm fills the table in a bottom-up manner, considering all possible substrings.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int longestPalindromicSubsequence(string s) {
    int n = s.length();
    vector<vector<int>> dp(n, vector<int>(n, 0));
    
    // All substrings with one character are palindromes
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }
    
    // Check for substring of length 2
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == s[i + 1]) {
            dp[i][i + 1] = 2;
        } else {
            dp[i][i + 1] = 1;
        }
    }
    
    // Check for lengths greater than 2
    for (int length = 3; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            if (s[i] == s[j]) {
                dp[i][j] = dp[i + 1][j - 1] + 2;
            } else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    
    return dp[0][n - 1];
}

int main() {
    string s = "banana";
    cout << "Length of the longest palindromic subsequence: " << longestPalindromicSubsequence(s);
    return 0;
}
```

## Test Cases
```
Input: "banana"
Output: 5
Input: "abc"
Output: 1
```

## Key Takeaways
- The dynamic programming approach is suitable for problems that have overlapping subproblems and optimal substructure.
- The 2D table helps to avoid redundant computation by storing the results of subproblems.
- The time complexity of O(n^2) is due to the nested loops used to fill the 2D table.