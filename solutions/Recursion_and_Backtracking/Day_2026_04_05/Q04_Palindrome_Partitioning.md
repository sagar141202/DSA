# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible palindrome partitions are `[["a", "a", "b"], ["aa", "b"]]`. The input string `s` consists only of lowercase English letters and the length of `s` is in the range `[1, 16]`.

## Approach
The problem can be solved using recursion and backtracking. The idea is to generate all possible partitions of the string and then check if each partition is a palindrome. We start by choosing the first partition, then recursively generate all possible partitions for the remaining string.

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
            if (s[left] != s[right]) return false;
            left++, right--;
        }
        return true;
    }
};

int main() {
    Solution solution;
    string input = "aab";
    vector<vector<string>> result = solution.partition(input);
    for (auto& partition : result) {
        for (auto& substr : partition) {
            cout << substr << " ";
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
- The problem requires generating all possible partitions of the input string and checking if each partition is a palindrome.
- Recursion and backtracking are used to generate all possible partitions.
- The time complexity is O(2^n * n) due to the recursive nature of the solution and the need to check if each substring is a palindrome.