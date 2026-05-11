# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The input string `s` consists of lowercase English letters and has a length of at most 10. The output should be a list of lists of strings, where each inner list represents a palindrome partition.

## Approach
The approach to solve this problem is to use recursion and backtracking. We iterate over the string, check if the substring is a palindrome, and if it is, we add it to the current partition and recursively call the function on the remaining substring. If the substring is not a palindrome, we backtrack and try a different partition.

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
    
    bool isPalindrome(string s) {
        int left = 0, right = s.length() - 1;
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
Input: "aab"
Output: [["a","a","b"],["aa","b"]]
Input: "abba"
Output: [["a","b","b","a"],["a","bb","a"],["abba"]]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible palindrome partitions.
- Check if a substring is a palindrome before adding it to the current partition.
- Backtrack when a substring is not a palindrome to try different partitions.