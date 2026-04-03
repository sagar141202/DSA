# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters, but they will be ignored. The input string will only contain parentheses, and the length of the string will be in the range [1, 1000].

## Approach
We will use a stack to keep track of the opening brackets and match them with the closing brackets. When we encounter a closing bracket, we check if the top of the stack contains the corresponding opening bracket. If it does, we pop the opening bracket from the stack. If it doesn't, or if the stack is empty, we return false.

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
        unordered_map<char, char> mp = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            } else if (c == ')' || c == ']' || c == '}') {
                if (st.empty() || st.top() != mp[c]) {
                    return false;
                }
                st.pop();
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
- Use a stack to keep track of the opening brackets.
- Use an unordered map to map closing brackets to their corresponding opening brackets.
- Return false as soon as a mismatch is found, or if there are remaining opening brackets in the stack after iterating over the entire string.