# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The input string `s` consists of lowercase English letters and the length of `s` is in the range `[1, 16]`.

## Approach
The approach is to use backtracking to generate all possible partitions of the string and check if each partition is a palindrome. We will use a helper function to check if a string is a palindrome. The algorithm will iterate over the string, generate all possible partitions, and add the valid palindrome partitions to the result.

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
        for (int end = start; end < s.size(); end++) {
            string substr = s.substr(start, end - start + 1);
            if (isPalindrome(substr)) {
                path.push_back(substr);
                backtrack(result, path, s, end + 1);
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
```

## Key Takeaways
- Use backtracking to generate all possible partitions of the string.
- Check if each partition is a palindrome using a helper function.
- Add the valid palindrome partitions to the result.