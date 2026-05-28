# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters, which should be ignored.

## Approach
We will use a stack to solve this problem. The idea is to push every opening bracket into the stack and whenever we encounter a closing bracket, we check if the top of the stack contains the corresponding opening bracket. If it does, we pop the opening bracket from the stack; otherwise, we return false.

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
        for (char c : s) {
            // if the character is an opening bracket, push it into the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            // if the character is a closing bracket, check if the stack is empty or the top of the stack does not match
            else if (c == ')' || c == '}' || c == ']') {
                if (st.empty()) {
                    return false;
                }
                char top = st.top();
                st.pop();
                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        // if the stack is empty after processing the entire string, the string is valid
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
- Check if the top of the stack matches the current closing bracket.
- If the stack is empty after processing the entire string, the string is valid.