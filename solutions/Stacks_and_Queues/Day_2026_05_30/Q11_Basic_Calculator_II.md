# Basic Calculator II

## Problem Statement
Given a string s which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers, '+', '-', '*', '/' operators and empty spaces. The integer division should truncate toward zero. You may assume that the given expression is always valid. A valid expression is one that can be parsed and evaluated to a result. Examples of valid expressions include "3+2*2", " 3/2 ", " 100/1 + 12 * 3 ", etc.

## Approach
We will use a stack-based approach to solve this problem, iterating through the string and applying operators to the top elements of the stack. We will handle the '*' and '/' operators immediately when encountered, and the '+' and '-' operators after iterating through the entire string.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> st;
        char sign = '+';
        int num = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
                if (sign == '+') {
                    st.push(num);
                } else if (sign == '-') {
                    st.push(-num);
                } else if (sign == '*') {
                    int pre = st.top();
                    st.pop();
                    st.push(pre * num);
                } else if (sign == '/') {
                    int pre = st.top();
                    st.pop();
                    st.push(pre / num);
                }
                sign = s[i];
                num = 0;
            }
        }
        int res = 0;
        while (!st.empty()) {
            res += st.top();
            st.pop();
        }
        return res;
    }
};
```

## Test Cases
```
Input: "3+2*2"
Output: 7
Input: " 3/2 "
Output: 1
Input: " 100/1 + 12 * 3 "
Output: 136
```

## Key Takeaways
- Use a stack to store intermediate results and apply operators to the top elements.
- Handle '*' and '/' operators immediately when encountered.
- Handle '+' and '-' operators after iterating through the entire string.