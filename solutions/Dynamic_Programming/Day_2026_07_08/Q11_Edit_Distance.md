# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `word1` and `word2`, find the edit distance between them. The strings only contain lowercase English letters. The length of `word1` and `word2` is at most 500. For example, the edit distance between "kitten" and "sitting" is 3: replace the "k" with "s", replace the "e" with "i", and append "g".

## Approach
We use dynamic programming to solve this problem by creating a 2D array `dp` where `dp[i][j]` represents the edit distance between the first `i` characters of `word1` and the first `j` characters of `word2`. We fill up the `dp` array in a bottom-up manner.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        // Initialize the base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }

        // Fill up the dp array
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                }
            }
        }

        return dp[m][n];
    }
};
```

## Test Cases
```
Input: word1 = "kitten", word2 = "sitting"
Output: 3
Input: word1 = "intention", word2 = "execution"
Output: 5
```

## Key Takeaways
- The edit distance problem can be solved using dynamic programming by creating a 2D array to store the edit distances between substrings.
- The base cases are when one of the strings is empty, in which case the edit distance is the length of the other string.
- The edit distance between two strings can be calculated by considering the minimum cost of insertion, deletion, and substitution operations.