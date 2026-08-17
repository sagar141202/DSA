# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The input string may contain other characters that are not brackets.

## Approach
We will use a stack to keep track of the opening brackets and match them with the closing brackets. When we encounter a closing bracket, we check if the top of the stack contains the corresponding opening bracket. If it does, we pop the opening bracket from the stack; otherwise, we return false. If we finish iterating over the string and the stack is empty, we return true; otherwise, we return false.

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
        
        // Iterate over each character in the string
        for (char c : s) {
            // If the character is an opening bracket, push it onto the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            // If the character is a closing bracket
            else if (c == ')' || c == '}' || c == ']') {
                // If the stack is empty, return false
                if (st.empty()) {
                    return false;
                }
                // Get the top of the stack
                char top = st.top();
                st.pop();
                // If the top of the stack does not match the closing bracket, return false
                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        // If the stack is empty after iterating over the string, return true; otherwise, return false
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
- Use a stack to match opening and closing brackets in a string.
- Iterate over the string and push opening brackets onto the stack.
- When encountering a closing bracket, check if the top of the stack contains the corresponding opening bracket.