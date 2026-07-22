# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `word1` and `word2`, find the edit distance between them. The strings only contain lowercase English letters. The length of `word1` is `m` and the length of `word2` is `n`, where `1 <= m, n <= 500`. The edit distance is calculated by considering the minimum cost of transforming `word1` into `word2` using the following operations: insert a character, delete a character, or replace a character.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the edit distance between the first `i` characters of `word1` and the first `j` characters of `word2`. The algorithm iterates through both strings and fills up the `dp` array based on the minimum cost of insertion, deletion, or substitution.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        
        // Create a 2D array to store the edit distances
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
                // Check if the current characters match
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Consider the minimum cost of insertion, deletion, or substitution
                    dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
                }
            }
        }
        
        // The edit distance is stored in the bottom-right corner of the dp array
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
- The edit distance problem can be solved using dynamic programming by maintaining a 2D array to store the edit distances between substrings.
- The algorithm has a time complexity of O(m*n) and a space complexity of O(m*n), where m and n are the lengths of the input strings.
- The solution iterates through both strings and fills up the dp array based on the minimum cost of insertion, deletion, or substitution.