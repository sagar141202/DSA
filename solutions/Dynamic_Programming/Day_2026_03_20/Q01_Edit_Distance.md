# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `word1` and `word2`, find the edit distance between them. The allowed operations are:
- Insertion: Insert a character into `word1`.
- Deletion: Delete a character from `word1`.
- Substitution: Replace a character in `word1` with a character from `word2`.
The edit distance is a measure of the similarity between two strings. For example, the edit distance between "kitten" and "sitting" is 3 (substitute "k" with "s", substitute "e" with "i", and append "g").

## Approach
The edit distance problem can be solved using dynamic programming, where we build a 2D table to store the edit distances between substrings of `word1` and `word2`. We fill the table in a bottom-up manner, using the previously computed values to compute the edit distance for the current substring.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

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
- The edit distance problem can be solved using dynamic programming, where we build a 2D table to store the edit distances between substrings.
- The time complexity of the solution is O(m * n), where m and n are the lengths of the input strings.
- The space complexity of the solution is O(m * n), which is used to store the 2D table.