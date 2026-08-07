# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The string `s` consists only of lowercase English letters and the length of `s` is in the range `[1, 16]`.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will generate all possible partitions of the string and check if each partition is a palindrome. If it is, we add it to our result.

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
        for (int end = start; end < s.size(); end++) {
            string substr = s.substr(start, end - start + 1);
            if (isPalindrome(substr)) {
                current.push_back(substr);
                backtrack(result, current, s, end + 1);
                current.pop_back();
            }
        }
    }

    bool isPalindrome(string s) {
        int left = 0;
        int right = s.size() - 1;
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

int main() {
    Solution solution;
    string s = "aab";
    vector<vector<string>> result = solution.partition(s);
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
Input: s = "aab"
Output: 
a a b 
aa b 
```

## Key Takeaways
- Use recursion and backtracking to generate all possible partitions of the string.
- Check if each partition is a palindrome using a helper function.
- Use a `start` index to keep track of the current position in the string.