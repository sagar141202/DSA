# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters, which should be ignored.

## Approach
The algorithm uses a stack to keep track of the opening brackets encountered so far. For each closing bracket, it checks if the top of the stack contains the corresponding opening bracket. If it does, the top is popped; otherwise, the string is invalid. The string is valid if the stack is empty at the end.

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
            // If opening bracket, push to stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            // If closing bracket, check if stack is empty or top does not match
            else if (c == ')' || c == '}' || c == ']') {
                if (st.empty()) return false;
                char top = st.top();
                st.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        // If stack is empty, all brackets were matched
        return st.empty();
    }
};
```

## Test Cases
```
Input: "([{}])"
Output: true
Input: "(]"
Output: false
Input: "([)]"
Output: false
```

## Key Takeaways
- Use a stack to keep track of opening brackets.
- Check for matching closing brackets and pop the corresponding opening bracket from the stack.
- The string is valid if the stack is empty at the end, indicating all brackets were properly matched.