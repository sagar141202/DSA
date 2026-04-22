# Basic Calculator II

## Problem Statement
Given a string s which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers, '+', '-', '*', '/' operators and empty spaces. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the eval built-in function.

## Approach
We will use a stack to store the intermediate results and operators. We iterate through the string, and when we encounter a number, we push it to the stack. When we encounter an operator, we pop the top two elements from the stack, apply the operation, and push the result back to the stack.

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
        int num = 0;
        char sign = '+';
        for (int i = 0; i < s.length(); i++) {
            // if current character is a digit, update the num
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            // if current character is not a digit or it's the last character
            if (!isdigit(s[i]) && s[i] != ' ' || i == s.length() - 1) {
                // if the sign is '+', push the num to the stack
                if (sign == '+') {
                    st.push(num);
                }
                // if the sign is '-', push the negative num to the stack
                else if (sign == '-') {
                    st.push(-num);
                }
                // if the sign is '*', pop the top element from the stack, multiply it with the num and push the result back to the stack
                else if (sign == '*') {
                    int top = st.top();
                    st.pop();
                    st.push(top * num);
                }
                // if the sign is '/', pop the top element from the stack, divide it by the num and push the result back to the stack
                else if (sign == '/') {
                    int top = st.top();
                    st.pop();
                    st.push(top / num);
                }
                // update the sign and reset the num
                sign = s[i];
                num = 0;
            }
        }
        // the result is the sum of all elements in the stack
        int result = 0;
        while (!st.empty()) {
            result += st.top();
            st.pop();
        }
        return result;
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
- Use a stack to store the intermediate results and operators.
- Handle the '*' and '/' operators first by popping the top element from the stack, applying the operation and pushing the result back to the stack.
- Handle the '+' and '-' operators by pushing the num to the stack with the correct sign.