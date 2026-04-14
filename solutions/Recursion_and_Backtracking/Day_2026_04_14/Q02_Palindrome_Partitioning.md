# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. Return all possible palindrome partitions of `s`. The input string `s` consists of lowercase English letters, and the length of `s` is between 1 and 20. For example, given the string "aab", the output should be `[["a", "a", "b"], ["aa", "b"]]`.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all possible partitions of the string and check if each partition is a palindrome. If it is, we add it to our result.

## Complexity
- Time: O(2^n * n) where n is the length of the string, because in the worst case, we generate all possible partitions of the string and check if each one is a palindrome.
- Space: O(n) for the recursion stack and to store the current partition.

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
        if (start == s.length()) {
            result.push_back(current);
            return;
        }

        for (int end = start; end < s.length(); end++) {
            string substr = s.substr(start, end - start + 1);
            if (isPalindrome(substr)) {
                current.push_back(substr);
                backtrack(result, current, s, end + 1);
                current.pop_back();
            }
        }
    }

    bool isPalindrome(string& s) {
        int left = 0, right = s.length() - 1;
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
Input: "aab"
Output: [["a", "a", "b"], ["aa", "b"]]
Input: "abba"
Output: [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible partitions of the string.
- Check if each partition is a palindrome before adding it to the result.
- Use a helper function `isPalindrome` to check if a string is a palindrome.