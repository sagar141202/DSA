# Longest Common Subsequence

## Problem Statement
The Longest Common Subsequence (LCS) problem is a classic problem in computer science, which involves finding the longest sequence that appears in the same order in two or more sequences. Given two sequences, X and Y, of lengths m and n respectively, the task is to find the length of their LCS and also to construct the LCS itself. For example, if X = "AGGTAB" and Y = "GXTXAYB", then the LCS of X and Y is "GTAB". The LCS problem has applications in data compression, pattern recognition, and bioinformatics.

## Approach
The LCS problem can be solved using dynamic programming, where a 2D table is constructed to store the lengths of LCS of subproblems. The table is filled in a bottom-up manner, and the final result is stored in the last cell of the table. The LCS itself can be constructed by tracing back the table from the last cell to the first cell.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int lcs(string X, string Y, int m, int n) {
    int L[m + 1][n + 1];

    // Build L[m+1][n+1] in bottom up fashion
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0)
                L[i][j] = 0;
            else if (X[i - 1] == Y[j - 1])
                L[i][j] = L[i - 1][j - 1] + 1;
            else
                L[i][j] = max(L[i - 1][j], L[i][j - 1]);
        }
    }

    // Following code is used to print LCS
    int index = L[m][n];
    string lcs_str;
    lcs_str.resize(index + 1);
    lcs_str[index] = '\0';

    int i = m;
    int j = n;
    while (i > 0 && j > 0) {
        if (X[i - 1] == Y[j - 1]) {
            lcs_str[index - 1] = X[i - 1];
            i--;
            j--;
            index--;
        }
        else if (L[i - 1][j] > L[i][j - 1])
            i--;
        else
            j--;
    }

    cout << "LCS: " << lcs_str.substr(0, lcs_str.size() - 1) << endl;
    return L[m][n];
}

int main() {
    string X = "AGGTAB";
    string Y = "GXTXAYB";
    int m = X.size();
    int n = Y.size();

    cout << "Length of LCS is " << lcs(X, Y, m, n) << endl;
    return 0;
}
```

## Test Cases
```
Input: X = "AGGTAB", Y = "GXTXAYB"
Output: Length of LCS is 4, LCS: GTAB
```

## Key Takeaways
- The LCS problem can be solved using dynamic programming with a time complexity of O(m*n) and space complexity of O(m*n).
- The LCS itself can be constructed by tracing back the table from the last cell to the first cell.
- The LCS problem has applications in data compression, pattern recognition, and bioinformatics.