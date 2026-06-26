# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters that are not brackets.

## Approach
Use a stack data structure to keep track of the opening brackets encountered so far. When a closing bracket is encountered, check if the top of the stack contains the corresponding opening bracket. If it does, pop the opening bracket from the stack; otherwise, return false. After iterating through the entire string, return true if the stack is empty (all brackets were matched correctly) and false otherwise.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> mp = {{')', '('}, {'}', '{'}, {']', '['}};
        
        for (char c : s) {
            if (mp.find(c) != mp.end()) {
                if (st.empty() || st.top() != mp[c]) {
                    return false;
                }
                st.pop();
            } else if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
        }
        
        return st.empty();
    }
};
```

## Test Cases
```
Input: "()"
Output: true
Input: "()[]{}"
Output: true
Input: "(]"
Output: false
Input: "([)]"
Output: false
Input: "{[]}"
Output: true
```

## Key Takeaways
- Use a stack to keep track of the opening brackets encountered so far.
- Use an unordered map to store the corresponding opening bracket for each closing bracket.
- Iterate through the string and check if the top of the stack contains the corresponding opening bracket when a closing bracket is encountered.