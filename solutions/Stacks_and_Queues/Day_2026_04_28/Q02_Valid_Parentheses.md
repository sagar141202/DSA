# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters that are not brackets.

## Approach
The problem can be solved using a stack data structure, where we push opening brackets onto the stack and pop them off when we encounter a matching closing bracket. If we encounter a closing bracket that does not match the top of the stack, or if there are brackets left on the stack at the end, the string is not valid.

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
        stack<char> stk;
        // Create a map to store the matching brackets
        unordered_map<char, char> mp = {{')', '('}, {']', '['}, {'}', '{'}};
        
        // Iterate over the string
        for (char c : s) {
            // If the character is an opening bracket, push it onto the stack
            if (c == '(' || c == '[' || c == '{') {
                stk.push(c);
            }
            // If the character is a closing bracket, check if the stack is empty or the top of the stack does not match
            else if (c == ')' || c == ']' || c == '}') {
                if (stk.empty() || stk.top() != mp[c]) {
                    return false;
                }
                // If the top of the stack matches, pop it off
                stk.pop();
            }
        }
        // If the stack is empty at the end, the string is valid
        return stk.empty();
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
- Use a map to store the matching brackets for easy lookup.
- Check for empty stack and matching brackets at each step to ensure the string is valid.