# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. Return all possible palindrome partitions of `s`. The input string `s` consists only of lowercase letters and has a length of at most 10. The output should be a list of lists of strings, where each inner list represents a palindrome partition.

## Approach
The solution uses recursion and backtracking to generate all possible partitions of the input string. It checks each substring to see if it's a palindrome and recursively generates all possible partitions of the remaining string.

## Complexity
- Time: O(2^n * n) where n is the length of the string, due to the recursive nature of the solution and the palindrome check.
- Space: O(n) for the recursive call stack and the space needed to store the current partition.

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
            if (isPalindrome(s, start, end)) {
                current.push_back(s.substr(start, end - start + 1));
                backtrack(s, end + 1, current, result);
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

int main() {
    Solution solution;
    string input = "aab";
    vector<vector<string>> result = solution.partition(input);
    for (const auto& partition : result) {
        for (const auto& str : partition) {
            cout << str << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: "aab"
Output: 
a a b 
aa b 
```

## Key Takeaways
- Use recursion and backtracking to generate all possible partitions of the input string.
- Check each substring to see if it's a palindrome before recursively generating all possible partitions of the remaining string.
- The time complexity is O(2^n * n) due to the recursive nature of the solution and the palindrome check.