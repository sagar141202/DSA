# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `str1` and `str2`, find the edit distance between them. The strings only contain lowercase English letters. The length of `str1` and `str2` can be up to 1000 characters.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents the edit distance between substrings of `str1` and `str2`. The edit distance is calculated by considering the minimum cost of insertion, deletion, and substitution at each step.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int editDistance(string str1, string str2) {
    int m = str1.size();
    int n = str2.size();
    
    // Create a 2D table to store the edit distances
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    
    // Initialize the base cases
    for (int i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    for (int j = 0; j <= n; j++) {
        dp[0][j] = j;
    }
    
    // Fill in the rest of the table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            // Check if the current characters match
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                // Calculate the minimum cost of insertion, deletion, and substitution
                dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
            }
        }
    }
    
    // The edit distance is stored in the bottom-right corner of the table
    return dp[m][n];
}
```

## Test Cases
```
Input: str1 = "kitten", str2 = "sitting"
Output: 3
Input: str1 = "hello", str2 = "world"
Output: 4
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The edit distance problem can be solved using a 2D table to store the edit distances between substrings.
- The time and space complexity of the solution are O(m*n), where m and n are the lengths of the input strings.