# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. Return all possible palindrome partitions of `s`. For example, given `s = "aab"`, the output should be `[["a", "a", "b"], ["aa", "b"]]`. The string `s` only contains lowercase English letters, and the length of `s` is in the range `[1, 16]`.

## Approach
The algorithm uses recursion and backtracking to generate all possible partitions of the input string and checks if each partition is a palindrome. If a partition is a palindrome, it is added to the result list. The base case for the recursion is when the start index reaches the end of the string.

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
            string substr = s.substr(start, end - start + 1);
            if (isPalindrome(substr)) {
                current.push_back(substr);
                backtrack(result, current, s, end + 1);
                current.pop_back();
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
Input: s = "aab"
Output: [["a", "a", "b"], ["aa", "b"]]
Input: s = "abba"
Output: [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible partitions of the input string.
- Check if each partition is a palindrome using a helper function.
- Use a base case to stop the recursion when the start index reaches the end of the string.