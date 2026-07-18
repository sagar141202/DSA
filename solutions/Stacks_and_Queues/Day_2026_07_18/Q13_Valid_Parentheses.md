# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid, but "(]" and "([)]" are not. The string may contain other characters that are not brackets.

## Approach
We can solve this problem using a stack data structure, where we push opening brackets onto the stack and pop them off when we encounter the corresponding closing bracket. If we encounter a closing bracket that doesn't match the top of the stack, or if there are items left on the stack at the end, the string is not valid.

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
        
        // Iterate over each character in the string
        for (char c : s) {
            // If the character is an opening bracket, push it onto the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            // If the character is a closing bracket, check if the stack is empty or the top of the stack doesn't match
            else if (c == ')' || c == '}' || c == ']') {
                if (st.empty() || st.top() != mp[c]) {
                    return false;
                }
                // If the top of the stack matches, pop it off
                st.pop();
            }
        }
        
        // If the stack is empty at the end, the string is valid
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
- Use a stack to keep track of opening brackets and match them with corresponding closing brackets.
- Use a map to store the corresponding closing brackets for each opening bracket.
- Check if the stack is empty or the top of the stack doesn't match when encountering a closing bracket.