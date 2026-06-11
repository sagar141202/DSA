# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `word1` and `word2`, find the edit distance between them. The strings only contain lowercase English letters. The length of `word1` and `word2` will be in the range `[0, 500]`. 

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents the edit distance between substrings of `word1` and `word2`. The edit distance is calculated by considering the minimum cost of insertion, deletion, or substitution at each step.

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
        int n = word1.size();
        int m = word2.size();
        // Create a 2D table to store the edit distances
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

        // Initialize the base cases
        for (int i = 0; i <= n; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= m; j++) {
            dp[0][j] = j;
        }

        // Fill in the rest of the table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                // Check if the current characters match
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Consider the minimum cost of insertion, deletion, or substitution
                    dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                }
            }
        }

        // The edit distance is stored in the bottom-right corner of the table
        return dp[n][m];
    }
};
```

## Test Cases
```
Input: word1 = "kitten", word2 = "sitting"
Output: 3
Input: word1 = "", word2 = ""
Output: 0
Input: word1 = "a", word2 = "b"
Output: 1
```

## Key Takeaways
- The edit distance problem can be solved using dynamic programming by building a 2D table to store the edit distances between substrings.
- The time complexity is O(n*m), where n and m are the lengths of the input strings.
- The space complexity is also O(n*m) due to the 2D table used to store the edit distances.