# Basic Calculator II

## Problem Statement
Given a string s which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers, '+', '-', '*', '/' operators and empty spaces. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the eval built-in function.

## Approach
We use a stack to store the intermediate results and operators. When we encounter a number, we push it to the stack. When we encounter an operator, we pop the top two numbers from the stack, apply the operation, and push the result back to the stack.

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
        for (int i = 0; i < s.size(); i++) {
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.size() - 1) {
                if (sign == '+') {
                    st.push(num);
                } else if (sign == '-') {
                    st.push(-num);
                } else if (sign == '*') {
                    int prev = st.top();
                    st.pop();
                    st.push(prev * num);
                } else if (sign == '/') {
                    int prev = st.top();
                    st.pop();
                    st.push(prev / num);
                }
                sign = s[i];
                num = 0;
            }
        }
        int sum = 0;
        while (!st.empty()) {
            sum += st.top();
            st.pop();
        }
        return sum;
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
- Use a stack to store intermediate results and operators.
- Handle the '*' and '/' operators immediately when encountered.
- Handle the '+' and '-' operators after iterating through the entire string.