# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. Return all possible palindrome partitions of `s`. For example, given `s = "aab"`, the output should be `[["a", "a", "b"], ["aa", "b"]]`. The string `s` consists only of lowercase English letters and the length of `s` is in the range `[1, 16]`.

## Approach
The algorithm uses backtracking to generate all possible partitions of the string. It checks if each substring is a palindrome and if so, adds it to the current partition. The function then recursively generates all possible partitions of the remaining substring.

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
        backtrack(s, 0, current, result);
        return result;
    }

    void backtrack(string s, int start, vector<string>& current, vector<vector<string>>& result) {
        if (start == s.size()) {
            result.push_back(current);
            return;
        }
        
        for (int end = start; end < s.size(); end++) {
            string substr = s.substr(start, end - start + 1);
            if (isPalindrome(substr)) {
                current.push_back(substr);
                backtrack(s, end + 1, current, result);
                current.pop_back();
            }
        }
    }

    bool isPalindrome(string s) {
        int left = 0, right = s.size() - 1;
        while (left < right) {
            if (s[left] != s[right]) {
                return false;
            }
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
- Check if each substring is a palindrome before adding it to the current partition.
- Use a helper function to check if a string is a palindrome.