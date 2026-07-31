# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The input string `s` consists only of lowercase English letters and has a length of at most 10.

## Approach
The approach to solve this problem involves using backtracking to generate all possible partitions of the input string and checking if each partition is a palindrome. We will use a recursive function to explore all possible partitions.

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
Output: [["a","a","b"],["aa","b"]]
Input: s = "abba"
Output: [["a","b","b","a"],["a","bb","a"],["abba"]]
```

## Key Takeaways
- Use backtracking to generate all possible partitions of the input string.
- Check if each partition is a palindrome by comparing characters from the start and end of the substring.
- Use a recursive function to explore all possible partitions and store the results in a vector.