# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters that are not brackets.

## Approach
We will use a stack data structure to keep track of the opening brackets and match them with the corresponding closing brackets. The algorithm will iterate over the string, pushing opening brackets onto the stack and popping them off when a matching closing bracket is encountered.

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
        
        // Create a map to store the matching brackets
        unordered_map<char, char> mp = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        // Iterate over the string
        for (char c : s) {
            // If the character is an opening bracket, push it onto the stack
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            }
            // If the character is a closing bracket, check if the stack is empty or the top of the stack does not match
            else if (c == ')' || c == ']' || c == '}') {
                if (st.empty() || st.top() != mp[c]) {
                    return false;
                }
                // If the top of the stack matches, pop it off
                st.pop();
            }
        }
        
        // If the stack is empty after iterating over the string, the string is valid
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
- Use a stack to keep track of the opening brackets and match them with the corresponding closing brackets.
- Iterate over the string and push opening brackets onto the stack, popping them off when a matching closing bracket is encountered.
- Use a map to store the matching brackets for easy lookup.