# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters that are not brackets.

## Approach
We will use a stack data structure to keep track of the opening brackets and match them with the corresponding closing brackets. When we encounter an opening bracket, we push it onto the stack. When we encounter a closing bracket, we check if the top of the stack contains the corresponding opening bracket.

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
        // Create a stack to store the opening brackets
        stack<char> st;
        
        // Create a map to store the corresponding closing brackets
        unordered_map<char, char> mp = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        // Iterate through the string
        for (char c : s) {
            // If the character is an opening bracket, push it onto the stack
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            }
            // If the character is a closing bracket, check if the top of the stack contains the corresponding opening bracket
            else if (c == ')' || c == ']' || c == '}') {
                if (st.empty() || st.top() != mp[c]) {
                    return false;
                }
                st.pop();
            }
        }
        
        // If the stack is empty, the string is valid
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
- Use a stack data structure to keep track of the opening brackets.
- Use a map to store the corresponding closing brackets.
- Iterate through the string and check for matching brackets.