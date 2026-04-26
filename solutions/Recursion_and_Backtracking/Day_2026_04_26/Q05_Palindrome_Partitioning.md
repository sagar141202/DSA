# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. The task is to return all possible palindrome partitions of the given string. For example, if the input string is "aab", the output will be `[["a", "a", "b"], ["aa", "b"]]`. The string `s` consists of lowercase English letters and the length of `s` is between 1 and 16.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all possible partitions of the string and check if each partition is a palindrome. If it is, we will add it to our result list. The algorithm will explore all possible partitions and filter out the ones that are not palindromes.

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
Input: "aab"
Output: [["a", "a", "b"], ["aa", "b"]]
Input: "abba"
Output: [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible partitions of a string.
- A helper function `isPalindrome` can be used to check if a substring is a palindrome.
- The time complexity is exponential due to the recursive nature of the algorithm, but it is necessary to explore all possible partitions.