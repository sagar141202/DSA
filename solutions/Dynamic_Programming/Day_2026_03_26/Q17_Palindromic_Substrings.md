# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in the string. A palindromic substring is a substring that reads the same backwards as forwards. For example, "aba" is a palindrome, but "abc" is not. The string will only contain lowercase English letters. The length of the string is between 1 and 1000 characters.

## Approach
The approach is to use dynamic programming to build a 2D table where each cell [i][j] represents whether the substring from index i to j is a palindrome or not. We then count the total number of palindromic substrings by iterating over the table.

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
- Use dynamic programming to solve problems that have overlapping subproblems.
- The dp table can be used to store the results of subproblems to avoid redundant computation.
- The time complexity of this solution is O(n^2) due to the nested loops, where n is the length of the string.