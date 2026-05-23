# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. Return all possible palindrome partitions of `s`. The input string `s` consists only of lowercase English letters. The length of `s` is in the range `[1, 16]`.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all possible partitions of the string and check if each partition is a palindrome. If it is, we will add it to our result.

## Complexity
- Time: O(2^n * n) where n is the length of the string, because in the worst case, we are generating all possible partitions of the string and checking if each partition is a palindrome.
- Space: O(n) for the recursion stack and to store the current partition.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(string s, int start, vector<string>& path, vector<vector<string>>& result) {
    if (start == s.size()) {
        result.push_back(path);
        return;
    }
    for (int i = start; i < s.size(); i++) {
        string str = s.substr(start, i - start + 1);
        if (str == string(str.rbegin(), str.rend())) {
            path.push_back(str);
            backtrack(s, i + 1, path, result);
            path.pop_back();
        }
    }
}

vector<vector<string>> partition(string s) {
    vector<vector<string>> result;
    vector<string> path;
    backtrack(s, 0, path, result);
    return result;
}

int main() {
    string s = "aab";
    vector<vector<string>> result = partition(s);
    for (auto& x : result) {
        for (auto& y : x) {
            cout << y << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: s = "aab"
Output: 
[["a", "a", "b"], 
 ["aa", "b"]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible partitions of the string.
- Check if each partition is a palindrome by comparing the string with its reverse.
- Use a helper function `backtrack` to generate all possible partitions and add them to the result if they are palindromes.