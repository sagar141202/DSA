# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The string `s` consists of lowercase English letters and has a length of at most 10. The task is to return all possible palindrome partitions of `s`.

## Approach
The problem can be solved using recursion and backtracking. We iterate over the string and for each character, we check if the substring from the start to the current index is a palindrome. If it is, we add it to the current partition and recursively call the function for the remaining substring.

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
    
    void backtrack(vector<vector<string>>& result, vector<string>& current, string s, int start) {
        if (start == s.size()) {
            result.push_back(current);
            return;
        }
        
        for (int i = start; i < s.size(); i++) {
            if (isPalindrome(s, start, i)) {
                current.push_back(s.substr(start, i - start + 1));
                backtrack(result, current, s, i + 1);
                current.pop_back();
            }
        }
    }
    
    bool isPalindrome(string s, int start, int end) {
        while (start < end) {
            if (s[start] != s[end]) {
                return false;
            }
            start++;
            end--;
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
- Use recursion and backtracking to generate all possible partitions of the string.
- Check if a substring is a palindrome by comparing characters from the start and end indices.
- Use a helper function `isPalindrome` to check if a substring is a palindrome.