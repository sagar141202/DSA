# Longest Palindromic Subsequence

## Problem Statement
Given a string, find the length of the longest palindromic subsequence. A palindromic subsequence is a sequence that is the same when its characters are reversed. The input string only contains lowercase English letters. The length of the input string is between 1 and 1000. For example, the longest palindromic subsequence of "banana" is "anana" with a length of 5.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell [i][j] represents the length of the longest palindromic subsequence in the substring from index i to j. The table is filled in a bottom-up manner by considering all possible substrings.

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
    
    // Fill the diagonal of the table with 1s, since a single character is a palindrome
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }
    
    // Fill the table in a bottom-up manner
    for (int length = 2; length <= n; length++) {
        for (int i = 0; i < n - length + 1; i++) {
            int j = i + length - 1;
            
            // If the first and last characters are the same, consider them as part of the palindrome
            if (s[i] == s[j]) {
                dp[i][j] = dp[i + 1][j - 1] + 2;
            } 
            // Otherwise, consider the maximum length without the first or last character
            else {
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);
            }
        }
    }
    
    // The length of the longest palindromic subsequence is stored in the top-right corner of the table
    return dp[0][n - 1];
}

int main() {
    string s = "banana";
    cout << longestPalindromicSubsequence(s) << endl;
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
- The dynamic programming approach allows for an efficient solution with a time complexity of O(n^2).
- The 2D table is used to store the lengths of the longest palindromic subsequences for all possible substrings.
- The table is filled in a bottom-up manner, considering all possible substrings and their corresponding palindromic subsequences.