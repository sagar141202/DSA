# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters that are not brackets, but they should be ignored. For example, "([)]" is not valid, but "{[]}" is valid.

## Approach
The problem can be solved using a stack data structure, where we push opening brackets into the stack and pop them when we encounter a matching closing bracket. If we encounter a closing bracket that does not match the top of the stack, or if there are unmatched opening brackets at the end, the string is not valid.

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
- Use a stack to keep track of opening brackets.
- Use an unordered map to store the mapping between closing and opening brackets.
- Iterate through the string, pushing opening brackets into the stack and popping them when a matching closing bracket is found.