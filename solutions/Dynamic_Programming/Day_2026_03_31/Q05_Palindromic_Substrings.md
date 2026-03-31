# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings. A palindromic substring is a substring that reads the same backward as forward. For example, in the string "abc", the palindromic substrings are "a", "b", and "c". In the string "aaa", the palindromic substrings are "a", "aa", "aaa". The string will contain only lowercase English letters and the length of the string will be in the range [1, 1000].

## Approach
The approach is to use dynamic programming to build a 2D table where each cell [i][j] represents whether the substring from i to j is a palindrome or not. We then count the number of True values in the table to get the total number of palindromic substrings. The algorithm iterates over the string, checking for palindromes of length 1, 2, and greater than 2.

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
- We use dynamic programming to solve this problem efficiently by storing the results of subproblems in a 2D table.
- The time complexity is O(n^2) because we are using two nested loops to fill the dp table.
- The space complexity is also O(n^2) for storing the dp table.