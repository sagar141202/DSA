# Edit Distance

## Problem Statement
The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions) required to change one string into the other. Given two strings `str1` and `str2`, find the edit distance between them. The strings only contain lowercase letters, and the length of each string is at most 100. For example, the edit distance between "kitten" and "sitting" is 3 (replace 'k' with 's', replace 'e' with 'i', and append 'g').

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the edit distances between substrings of `str1` and `str2`. We fill the table in a bottom-up manner, considering all possible operations at each step. The edit distance between the two strings is stored in the last cell of the table.

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
    int dp[m + 1][n + 1];

    // Initialize the first row and column
    for (int i = 0; i <= m; i++)
        dp[i][0] = i;
    for (int j = 0; j <= n; j++)
        dp[0][j] = j;

    // Fill the rest of the table
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (str1[i - 1] == str2[j - 1])
                dp[i][j] = dp[i - 1][j - 1];
            else
                dp[i][j] = 1 + min(min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]);
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
- The edit distance problem can be solved using dynamic programming by creating a 2D table to store the edit distances between substrings.
- The table is filled in a bottom-up manner, considering all possible operations at each step.
- The edit distance between the two strings is stored in the last cell of the table.