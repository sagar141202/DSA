# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The input string `s` consists of only lowercase English letters and the length of `s` is in the range `[1, 16]`.

## Approach
The approach to solve this problem is to use backtracking and recursion to generate all possible partitions of the input string. We will check if each substring is a palindrome and if it is, we will add it to the current partition.

## Complexity
- Time: O(2^n * n) where n is the length of the input string, because in the worst case, we have to generate all possible partitions of the string.
- Space: O(n) for the recursion stack and the space needed to store the current partition.

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
- Use backtracking and recursion to generate all possible partitions of the input string.
- Check if each substring is a palindrome before adding it to the current partition.
- The time complexity is exponential due to the generation of all possible partitions, but the space complexity is linear due to the recursion stack and the space needed to store the current partition.