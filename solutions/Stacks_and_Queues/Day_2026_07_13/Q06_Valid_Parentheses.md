# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters that are not brackets.

## Approach
We can use a stack to solve this problem by pushing opening brackets onto the stack and popping them off when we encounter a matching closing bracket. If we encounter a closing bracket that doesn't match the top of the stack, or if there are items left on the stack at the end, the string is not valid.

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
        stack<char> stack;
        
        // Create a map to store the corresponding closing brackets
        unordered_map<char, char> map = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        // Iterate over the string
        for (char c : s) {
            // If the character is an opening bracket, push it onto the stack
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            }
            // If the character is a closing bracket, check if it matches the top of the stack
            else if (c == ')' || c == ']' || c == '}') {
                // If the stack is empty or the top of the stack doesn't match, return false
                if (stack.empty() || stack.top() != map[c]) {
                    return false;
                }
                // Otherwise, pop the top of the stack
                stack.pop();
            }
        }
        
        // If the stack is empty, the string is valid
        return stack.empty();
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
- Use a map to store the corresponding closing brackets.
- Iterate over the string and push opening brackets onto the stack, and pop them off when a matching closing bracket is encountered.