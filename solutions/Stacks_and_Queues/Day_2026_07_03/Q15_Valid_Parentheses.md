# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The input string may contain letters and other characters, which should be ignored. For example, "([a])" is valid but "([a" is not.

## Approach
We will use a stack data structure to keep track of the opening brackets and match them with the corresponding closing brackets. When we encounter an opening bracket, we push it onto the stack. When we encounter a closing bracket, we check if the top of the stack contains the corresponding opening bracket. If it does, we pop the opening bracket from the stack. If it doesn't, or if the stack is empty, we return false.

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
            // if opening bracket, push onto stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            // if closing bracket, check if stack is empty or top of stack does not match
            else if (c == ')' || c == '}' || c == ']') {
                if (st.empty()) return false;
                char top = st.top();
                st.pop();
                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        // if stack is empty after iterating through string, then parentheses are valid
        return st.empty();
    }
};
```

## Test Cases
```
Input: "([)]"
Output: false
Input: "([])"
Output: true
Input: "([a])"
Output: true
```

## Key Takeaways
- Use a stack to keep track of opening brackets and match them with corresponding closing brackets.
- Check if the top of the stack contains the corresponding opening bracket when encountering a closing bracket.
- If the stack is empty after iterating through the string, then the parentheses are valid.