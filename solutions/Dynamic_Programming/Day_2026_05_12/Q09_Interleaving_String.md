# Interleaving String

## Problem Statement
Given three strings: `s1`, `s2`, and `s3`, determine if `s3` is an interleaving of `s1` and `s2`. An interleaving of two strings is a string that contains all characters of both strings and the order of characters in each string is preserved. If `s3` is an interleaving of `s1` and `s2`, return `true`; otherwise, return `false`. The length of `s1`, `s2`, and `s3` are `m`, `n`, and `m + n` respectively.

## Approach
We will use dynamic programming to solve this problem by checking all possible interleavings of `s1` and `s2` and comparing them with `s3`. We will create a 2D table where each cell represents whether the corresponding substrings of `s1` and `s2` can interleave to form the corresponding substring of `s3`. 

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size();
        int n = s2.size();
        
        // If the lengths of s1 and s2 do not add up to the length of s3, 
        // then s3 cannot be an interleaving of s1 and s2.
        if (m + n != s3.size()) {
            return false;
        }
        
        // Create a 2D table to store the results of subproblems.
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Initialize the base cases.
        dp[0][0] = true;
        
        // Fill the first row of the table.
        for (int j = 1; j <= n; j++) {
            dp[0][j] = dp[0][j - 1] && s2[j - 1] == s3[j - 1];
        }
        
        // Fill the first column of the table.
        for (int i = 1; i <= m; i++) {
            dp[i][0] = dp[i - 1][0] && s1[i - 1] == s3[i - 1];
        }
        
        // Fill the rest of the table.
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // If the current character in s3 matches the current character in s1, 
                // then we can interleave the substrings of s1 and s2 up to the current characters.
                // If the current character in s3 matches the current character in s2, 
                // then we can interleave the substrings of s1 and s2 up to the current characters.
                dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]) || (dp[i][j - 1] && s2[j - 1] == s3[i + j - 1]);
            }
        }
        
        // The answer is stored in the bottom-right cell of the table.
        return dp[m][n];
    }
};

int main() {
    Solution solution;
    string s1 = "aabcc";
    string s2 = "dbbca";
    string s3 = "aadbbcbcac";
    cout << solution.isInterleave(s1, s2, s3) << endl;
    return 0;
}
```

## Test Cases
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The key to solving this problem is to recognize that it can be broken down into smaller subproblems, each of which can be solved independently.
- The use of a 2D table to store the results of subproblems allows us to avoid redundant computation and improve the efficiency of the solution.