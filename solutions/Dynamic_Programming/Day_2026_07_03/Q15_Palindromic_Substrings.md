# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in it. A palindromic substring is a substring that reads the same backward as forward. For example, in the string "abc", there are 3 palindromic substrings: "a", "b", and "c". In the string "aaa", there are 6 palindromic substrings: "a", "a", "a", "aa", "aa", and "aaa". The input string will only contain lowercase English letters.

## Approach
The approach to solve this problem is to use dynamic programming to store whether each substring is palindromic or not. We will iterate over all possible substrings and check if they are palindromic. If a substring is palindromic, we will increment the count of palindromic substrings.

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
        
        // All substrings with one character are palindromes
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
            count++;
        }
        
        // Check for substrings of length 2
        for (int i = 0; i < n - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp[i][i + 1] = true;
                count++;
            }
        }
        
        // Check for lengths greater than 2
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
- We use a 2D boolean array `dp` to store whether each substring is palindromic or not.
- We start by marking all substrings with one character as palindromes and then check for substrings of length 2 and greater.
- We use a bottom-up dynamic programming approach to fill the `dp` array and count the number of palindromic substrings.