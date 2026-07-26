# Palindrome Partitioning

## Problem Statement
Given a string `s`, partition `s` into all possible palindrome partitions. A palindrome partition is a partition where every substring is a palindrome. For example, given `s = "aab"`, the possible palindrome partitions are `["a", "a", "b"]` and `["aa", "b"]`. The function should return all possible palindrome partitions of the input string.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will iterate over the string and check if the substring is a palindrome. If it is, we will add it to the current partition and recursively call the function on the remaining substring.

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

int main() {
    Solution solution;
    string s = "aab";
    vector<vector<string>> result = solution.partition(s);
    for (auto& partition : result) {
        for (auto& str : partition) {
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
- The problem can be solved using recursion and backtracking.
- We need to check if a substring is a palindrome before adding it to the current partition.
- The time complexity is O(2^n * n) due to the recursive calls and the palindrome check.