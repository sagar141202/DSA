# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. Return all possible palindrome partitions of `s`. For example, given `s = "aab"`, the output should be `[["a", "a", "b"], ["aa", "b"]]`. The string `s` consists of lowercase English letters only.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all possible partitions of the string and check if each partition is a palindrome. If it is, we will add it to the result.

## Complexity
- Time: O(2^n * n) where n is the length of the string, because in the worst case, we have to generate all possible partitions of the string.
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
            string substring = s.substr(start, end - start + 1);
            if (isPalindrome(substring)) {
                current.push_back(substring);
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
- Use recursion and backtracking to generate all possible partitions of the string.
- Check if each partition is a palindrome before adding it to the result.
- Use a helper function `isPalindrome` to check if a string is a palindrome.