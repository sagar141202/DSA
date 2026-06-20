# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters that are not brackets, which can be ignored.

## Approach
We can use a stack to keep track of the opening brackets and pop them when we encounter a matching closing bracket. If we encounter a closing bracket that does not match the top of the stack, or if there are items left in the stack at the end, the string is not valid.

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
        unordered_map<char, char> mp = {{')', '('}, {']', '['}, {'}', '{'}};
        
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
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
- Use an unordered map to store the matching brackets for easy lookup.
- Always check if the stack is empty before popping to avoid runtime errors.