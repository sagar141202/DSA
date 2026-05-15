# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `str1` and `str2` of lengths `m` and `n`, find the edit distance between them. The allowed operations are: insert a character, delete a character, and replace a character. For example, the edit distance between "kitten" and "sitting" is 3 (replace 'k' with 's', replace 'e' with 'i', and append 'g').

## Approach
The algorithm uses dynamic programming to build a 2D table where each cell represents the edit distance between substrings of `str1` and `str2`. The final edit distance is stored in the bottom-right cell of the table. The table is filled in a bottom-up manner by considering the minimum cost of insertion, deletion, and substitution at each step.

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

    // Create a table to store results of sub-problems
    int dp[m + 1][n + 1];

    // Initialize the first row and column
    for (int i = 0; i <= m; i++)
        dp[i][0] = i;
    for (int j = 0; j <= n; j++)
        dp[0][j] = j;

    // Fill the table in a bottom-up manner
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i - 1] == str2[j - 1])
                dp[i][j] = dp[i - 1][j - 1];
            else
                dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i][j - 1], dp[i - 1][j - 1]));
        }
    }

    return dp[m][n];
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
- The edit distance problem can be solved using dynamic programming with a time complexity of O(m*n).
- The 2D table is filled in a bottom-up manner by considering the minimum cost of insertion, deletion, and substitution at each step.
- The final edit distance is stored in the bottom-right cell of the table.