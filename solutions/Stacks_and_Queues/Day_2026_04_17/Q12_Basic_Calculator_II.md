# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression is composed of digits and operators (`+`, `-`, `*`, `/`). The expression does not contain any parentheses. The division operator `/` is used for integer division, i.e., the result of division will be rounded towards zero. It is guaranteed that the input expression is valid and the result of the expression is within the range of 32-bit signed integer.

## Approach
We can use a stack to store the intermediate results. We iterate through the string, and whenever we encounter a digit, we update the current number. When we encounter an operator, we calculate the result based on the current operator and the top element of the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int calculate(string s) {
    stack<int> st;
    int curr = 0;
    char op = '+';
    for (int i = 0; i < s.size(); i++) {
        if (isdigit(s[i])) {
            curr = curr * 10 + (s[i] - '0');
        }
        if (!isdigit(s[i]) && s[i] != ' ' || i == s.size() - 1) {
            if (op == '+') {
                st.push(curr);
            } else if (op == '-') {
                st.push(-curr);
            } else if (op == '*') {
                st.push(st.top() * curr);
                st.pop();
            } else if (op == '/') {
                st.push(st.top() / curr);
                st.pop();
            }
            op = s[i];
            curr = 0;
        }
    }
    int res = 0;
    while (!st.empty()) {
        res += st.top();
        st.pop();
    }
    return res;
}
```

## Test Cases
```
Input: "3+2*2"
Output: 7
Input: " 3/2 "
Output: 1
Input: " 3+5 / 2 "
Output: 5
```

## Key Takeaways
- Use a stack to store the intermediate results.
- Update the current number whenever a digit is encountered.
- Calculate the result based on the current operator and the top element of the stack when an operator is encountered.