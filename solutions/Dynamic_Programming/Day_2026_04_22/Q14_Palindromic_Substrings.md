# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in the string. A palindromic substring is a substring that reads the same backward as forward. The string only contains lowercase English letters. The length of the string is at most 1000 characters. For example, in the string "abc", there are 3 palindromic substrings: "a", "b", and "c". In the string "aaa", there are 6 palindromic substrings: "a", "a", "a", "aa", "aa", and "aaa".

## Approach
The approach to solve this problem is to use dynamic programming to store whether each substring is palindromic or not. We will iterate over the string and check for palindromic substrings of lengths 1, 2, and greater than 2. For lengths greater than 2, we will use the previously computed values to determine if the substring is palindromic.

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
        int n = s.length();
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
- Use dynamic programming to store whether each substring is palindromic or not.
- Iterate over the string and check for palindromic substrings of lengths 1, 2, and greater than 2.
- For lengths greater than 2, use the previously computed values to determine if the substring is palindromic.