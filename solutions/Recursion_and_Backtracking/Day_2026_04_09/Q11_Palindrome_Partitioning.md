# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. Return all possible palindrome partitions of `s`. The input string `s` consists only of lowercase letters and has a length of at most 10. The output should be a list of lists of strings, where each inner list represents a palindrome partition.

## Approach
The approach to solve this problem is to use backtracking to generate all possible partitions of the string and then check if each partition is a palindrome. We will use a helper function to check if a string is a palindrome. The algorithm will recursively try all possible partitions and add them to the result if they are palindromes.

## Complexity
- Time: O(2^n * n) where n is the length of the string, as there are 2^n possible partitions and checking if a string is a palindrome takes O(n) time.
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
- Use backtracking to generate all possible partitions of the string.
- Check if each partition is a palindrome using a helper function.
- Use a recursion stack to store the current partition and add it to the result if it is a palindrome.