# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into another. Given two strings `str1` and `str2`, find the edit distance between them. The strings only contain lowercase English letters. The length of `str1` and `str2` can be up to 100 characters.

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents the edit distance between substrings of `str1` and `str2`. The edit distance is calculated by considering the minimum cost of insertion, deletion, and substitution at each step.

## Complexity
- Time: O(n*m)
- Space: O(n*m)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int editDistance(string str1, string str2) {
    int n = str1.length();
    int m = str2.length();
    
    // Create a 2D table to store the edit distances
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    
    // Initialize the base cases
    for (int i = 0; i <= n; i++) {
        dp[i][0] = i;
    }
    for (int j = 0; j <= m; j++) {
        dp[0][j] = j;
    }
    
    // Fill the table in a bottom-up manner
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            // If the current characters match, no operation is needed
            if (str1[i - 1] == str2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                // Consider the minimum cost of insertion, deletion, and substitution
                dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]));
            }
        }
    }
    
    // The edit distance is stored in the bottom-right cell of the table
    return dp[n][m];
}

int main() {
    string str1 = "kitten";
    string str2 = "sitting";
    cout << "Edit Distance: " << editDistance(str1, str2) << endl;
    return 0;
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
- The table is filled in a bottom-up manner, considering the minimum cost of insertion, deletion, and substitution at each step.
- The edit distance is stored in the bottom-right cell of the table.