# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into another. Given two strings `str1` and `str2`, find the edit distance between them. The strings only contain lowercase English letters. The length of `str1` and `str2` can be up to 1000 characters. For example, the edit distance between "kitten" and "sitting" is 3 (replace 'k' with 's', replace 'e' with 'i', append 'g').

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the edit distance between substrings of `str1` and `str2`. We fill the table in a bottom-up manner by considering all possible operations (insertion, deletion, substitution) and choosing the one with the minimum cost.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int editDistance(string str1, string str2) {
    int m = str1.length();
    int n = str2.length();
    
    // Create a 2D table to store the edit distances
    vector<vector<int>> dp(m + 1, vector<int>(n + 1));
    
    // Initialize the base cases
    for (int i = 0; i <= m; i++) {
        dp[i][0] = i;
    }
    for (int j = 0; j <= n; j++) {
        dp[0][j] = j;
    }
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]));
            }
        }
    }
    
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
- The edit distance problem can be solved using dynamic programming by building a 2D table.
- The time complexity of the solution is O(m*n), where m and n are the lengths of the input strings.
- The space complexity of the solution is O(m*n), which is used to store the 2D table.