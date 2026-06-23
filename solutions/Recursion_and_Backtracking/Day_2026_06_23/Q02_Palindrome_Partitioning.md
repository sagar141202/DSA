# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible partitions are `["a", "a", "b"]` and `["aa", "b"]`.

## Approach
We will use backtracking to generate all possible partitions of the string and check if each partition is a palindrome. The idea is to start with an empty partition and add substrings one by one, checking if the current substring is a palindrome.

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
            left++;
            right--;
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
- Use backtracking to generate all possible partitions of the string.
- Check if each substring is a palindrome before adding it to the current partition.
- Use a helper function `isPalindrome` to check if a string is a palindrome.