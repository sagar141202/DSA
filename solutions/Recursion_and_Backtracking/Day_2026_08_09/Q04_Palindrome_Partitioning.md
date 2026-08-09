# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The input string `s` consists only of lowercase English letters and the length of `s` is in the range `[1, 16]`.

## Approach
The approach to solve this problem is to use backtracking to generate all possible partitions of the string and then check if each partition is a palindrome. We will use a helper function to check if a string is a palindrome and another helper function to generate all possible partitions.

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
        vector<string> path;
        backtrack(result, path, s, 0);
        return result;
    }

    void backtrack(vector<vector<string>>& result, vector<string>& path, string& s, int start) {
        if (start == s.size()) {
            result.push_back(path);
            return;
        }
        for (int i = start; i < s.size(); i++) {
            string substr = s.substr(start, i - start + 1);
            if (isPalindrome(substr)) {
                path.push_back(substr);
                backtrack(result, path, s, i + 1);
                path.pop_back();
            }
        }
    }

    bool isPalindrome(string& s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) return false;
            left++, right--;
        }
        return true;
    }
};
```

## Test Cases
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Input: s = "abba"
Output: [["a","b","b","a"],["a","bb","a"],["abba"]]
```

## Key Takeaways
- Use backtracking to generate all possible partitions of the string.
- Use a helper function to check if a string is a palindrome.
- The time complexity is exponential due to the backtracking, but the space complexity is linear due to the recursive call stack.