# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The function should return true if the string is valid and false otherwise. For example, the input "()" should return true, while the input "(]" should return false.

## Approach
We can use a stack data structure to solve this problem. We iterate through the string, pushing opening brackets onto the stack and popping the corresponding opening bracket when we encounter a closing bracket. If the stack is empty when we encounter a closing bracket or if the top of the stack does not match the closing bracket, we return false.

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
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else {
                if (st.empty()) return false;
                char top = st.top();
                st.pop();
                if ((c == ')' && top != '(') || (c == '}' && top != '{') || (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        return st.empty();
    }
};
```

## Test Cases
```
Input: "()"
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
- Iterate through the string, pushing opening brackets onto the stack and popping the corresponding opening bracket when a closing bracket is encountered.
- If the stack is empty when a closing bracket is encountered or if the top of the stack does not match the closing bracket, the string is not valid.