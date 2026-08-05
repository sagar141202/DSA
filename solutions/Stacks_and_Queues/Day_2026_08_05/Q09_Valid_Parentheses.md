# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters that are not brackets.

## Approach
The problem can be solved using a stack data structure, where we push opening brackets onto the stack and pop them off when we encounter a matching closing bracket. We use a hashmap to keep track of the corresponding closing bracket for each opening bracket. If we encounter a closing bracket that does not match the top of the stack, we return false.

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
        // Create a hashmap to store the corresponding closing bracket for each opening bracket
        unordered_map<char, char> bracketMap = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        // Create a stack to store the opening brackets
        stack<char> stack;
        
        // Iterate over the string
        for (char c : s) {
            // If the character is an opening bracket, push it onto the stack
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            }
            // If the character is a closing bracket, check if it matches the top of the stack
            else if (c == ')' || c == ']' || c == '}') {
                // If the stack is empty or the top of the stack does not match the closing bracket, return false
                if (stack.empty() || stack.top() != bracketMap[c]) {
                    return false;
                }
                // Otherwise, pop the top of the stack
                stack.pop();
            }
        }
        
        // If the stack is empty after iterating over the string, return true
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
- Use a stack to keep track of the opening brackets
- Use a hashmap to store the corresponding closing bracket for each opening bracket
- Iterate over the string and check if each character is a valid bracket