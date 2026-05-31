# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the output should be `[["a", "a", "b"], ["aa", "b"]]` because both `"a"` and `"aa"` are palindromes, and `"b"` is also a palindrome. The input string `s` will only contain lowercase letters, and the length of `s` will be in the range `[1, 16]`.

## Approach
The solution uses recursion and backtracking to generate all possible partitions of the input string. It checks if each substring is a palindrome and adds it to the current partition if it is. The algorithm explores all possible partitions by recursively calling itself with the remaining substring.

## Complexity
- Time: O(2^n * n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> current;
        backtrack(result, current, s, 0);
        return result;
    }

    void backtrack(vector<vector<string>>& result, vector<string>& current, string& s, int start) {
        if (start == s.size()) {
            result.push_back(current);
            return;
        }

        for (int end = start; end < s.size(); end++) {
            if (isPalindrome(s, start, end)) {
                current.push_back(s.substr(start, end - start + 1));
                backtrack(result, current, s, end + 1);
                current.pop_back();
            }
        }
    }

    bool isPalindrome(string& s, int start, int end) {
        while (start < end) {
            if (s[start++] != s[end--]) {
                return false;
            }
        }
        return true;
    }
};
```

## Test Cases
```
Input: s = "aab"
Output: [["a", "a", "b"], ["aa", "b"]]
Input: s = "abba"
Output: [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible partitions of the input string.
- Check if each substring is a palindrome before adding it to the current partition.
- Explore all possible partitions by recursively calling the backtrack function with the remaining substring.