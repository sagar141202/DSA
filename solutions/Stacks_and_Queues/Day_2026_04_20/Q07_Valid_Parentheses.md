# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The input string may contain other characters that are not brackets, and these characters should be ignored.

## Approach
The algorithm uses a stack data structure to keep track of the opening brackets. When a closing bracket is encountered, the top of the stack is checked to see if it contains the corresponding opening bracket. If it does, the top element is popped from the stack. If it doesn't, the string is not valid.

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
        unordered_map<char, char> mp = {{')', '('}, {'}', '{'}, {']', '['}};
        
        // Iterate over the string
        for (char c : s) {
            // If the character is an opening bracket, push it to the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            // If the character is a closing bracket, check if the stack is empty or the top element does not match
            else if (c == ')' || c == '}' || c == ']') {
                if (st.empty() || st.top() != mp[c]) {
                    return false;
                }
                // If the top element matches, pop it from the stack
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
- Use a stack data structure to keep track of the opening brackets.
- Use a map to store the corresponding closing brackets for easy lookup.
- Iterate over the string and push opening brackets to the stack, and pop the top element when a matching closing bracket is encountered.