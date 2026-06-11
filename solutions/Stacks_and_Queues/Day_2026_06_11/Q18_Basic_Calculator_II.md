# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces. The integer division should truncate toward zero. For example, `11 / 3 = 3`, `12 / 3 = 4`. You can assume that the given expression is always valid.

## Approach
We will use a stack to store the intermediate results. We iterate over the string and whenever we encounter a number, we push it into the stack. When we encounter an operator, we pop the last two elements from the stack, apply the operation and push the result back into the stack.

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
            // if the current character is a digit, update the num
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            // if the current character is not a digit or we have reached the end of the string
            if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
                // evaluate the expression based on the sign
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
                // update the sign and reset the num
                sign = s[i];
                num = 0;
            }
        }
        // calculate the final result
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
Input: " 3+5 / 2 "
Output: 5
```

## Key Takeaways
- Use a stack to store the intermediate results.
- Handle the operators `+`, `-`, `*`, `/` separately.
- Be careful with the integer division and the order of operations.