# Palindromic Substrings

## Problem Statement
Given a string, count the total number of palindromic substrings. A palindromic substring is a substring that reads the same backward as forward. The string only contains lowercase English letters. For example, "abc" has 3 palindromic substrings: "a", "b", and "c". The string "aaa" has 6 palindromic substrings: "a", "a", "a", "aa", "aa", and "aaa".

## Approach
The approach is to use dynamic programming to build a table where each cell [i][j] represents whether the substring from index i to j is a palindrome or not. We then count the number of True values in the table.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        int count = 0;
        
        // all substrings with one character are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }
        
        // check for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }
        
        // check for lengths greater than 2
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                if (s[i] == s[j] && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    count++;
                }
            }
        }
        
        return count;
    }
};
```

## Test Cases
```
Input: "abc"
Output: 3
Input: "aaa"
Output: 6
```

## Key Takeaways
- We use a dynamic programming table to store whether each substring is a palindrome or not.
- The time complexity is O(n^2) because we need to fill up the table of size n x n.
- The space complexity is also O(n^2) for the same reason.