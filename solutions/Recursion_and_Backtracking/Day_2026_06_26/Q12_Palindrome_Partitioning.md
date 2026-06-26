# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The input string `s` consists of lowercase English letters, and the length of `s` is in the range `[1, 16]`.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will iterate over the string and check if the substring is a palindrome. If it is, we will add it to the current partition and recursively call the function for the remaining substring.

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
Input: "aab"
Output: [["a","a","b"],["aa","b"]]
Input: "abba"
Output: [["a","b","b","a"],["a","bb","a"],["abba"]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible partitions of the string.
- Check if a substring is a palindrome using a helper function `isPalindrome`.
- Use a `backtrack` function to explore all possible partitions and add them to the result if the current partition is valid.